from django.db import models


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
    def get_by_natural_key(self, type):
        return self.get(tipo=type)