from django.db import models, connection


class AccountManager(models.Manager):
    use_for_related_fields = True

    def get_by_natural_key(self, name_accoun):
        return self.get(name_account=name_accoun)

    def saldo_final(self, **kwargs):
        consulta = "select account.id, account.created, " \
                   "account.name_account, " \
                   "account.saldo_actual, " \
                   "account.user_profile_id, " \
                   "account.account_type, ((account.saldo_actual - " \
                   "(COALESCE(gastos , 0) +  " \
                   "COALESCE(obligaciones, 0))) + " \
                   "COALESCE(ingresos, 0)) as saldo_total " \
                   "from incomes_account as account " \
                   "FULL JOIN (select account_id, " \
                   "sum(valor_ingreso)as ingresos " \
                   "from incomes_income group by account_id) " \
                   "income ON income.account_id = account.id " \
                   "FULL JOIN (select account_id, sum(value_expense) " \
                   "as gastos from expenses_expense group by account_id) " \
                   "expense ON expense.account_id = account.id " \
                   "FULL JOIN (select account_id, " \
                   "sum(value_obligation) as obligaciones " \
                   "from obligations_obligation where completed = 't' " \
                   "group by account_id) " \
                   "obligation " \
                   "ON obligation.account_id = account.id " \
                   "where account.user_profile_id = {0};"
        return self.raw(consulta.format(kwargs['user_id']))


class TypeIncomeManager(models.Manager):
    def get_by_natural_key(self, tipo):
        return self.get(tipo=tipo)


class IcomeManager(models.Manager):
    use_for_related_fields = True

    def total_group_account(self, **kwargs):
        fecha_i = kwargs['fecha_i']
        fecha_f = kwargs['fecha_f']
        consulta = "select account.name_account, sum(income.valor_ingreso) " \
                   "as total from incomes_income as income " \
                   "full Join  incomes_account as account " \
                   "ON income.account_id = account.id " \
                   "where income.user_profile_id = {0} and " \
                   "income.created between '{1}-{2}-{3}' and '{4}-{5}-{6}' " \
                   "group by account.name_account"
        cursor = connection.cursor()
        cursor.execute(consulta.format(kwargs['user_profile'],
                                       fecha_i.year,
                                       fecha_i.month,
                                       1,
                                       fecha_f.year,
                                       fecha_f.month,
                                       fecha_f.day))
        rows = self.dictfetchall(cursor)

        return rows

    def total_group_type(self, **kwargs):
        fecha_i = kwargs['fecha_i']
        fecha_f = kwargs['fecha_f']

        consulta = "select tipo_i.tipo,sum(income.valor_ingreso) " \
                   "as total from incomes_income as income " \
                   "FULL JOIN incomes_typeincome AS " \
                   "tipo_i ON income.type_income_id = " \
                   "tipo_i.id where income.user_profile_id = {0} " \
                   "and income.created between '{1}-{2}-{3}' " \
                   "and '{4}-{5}-{6}' group by tipo_i.tipo"
        cursor = connection.cursor()
        cursor.execute(consulta.format(kwargs['user_profile'],
                                       fecha_i.year,
                                       fecha_i.month,
                                       1,
                                       fecha_f.year,
                                       fecha_f.month,
                                       fecha_f.day))
        rows = self.dictfetchall(cursor)

        return rows

    def dictfetchall(self, cursor):
        """Return all rows from a cursor as a dict"""
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]
