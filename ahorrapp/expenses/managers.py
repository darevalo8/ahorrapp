from django.db import models, connection


class TypeExpenseManager(models.Manager):
    def get_by_natural_key(self, tipo):
        return self.get(type=tipo)


class ExpenseManager(models.Manager):
    use_for_related_fields = True

    def total_group_account(self, **kwargs):
        fecha_i = kwargs['fecha_i']
        fecha_f = kwargs['fecha_f']
        consulta = "select account.name_account, sum(expense.value_expense) " \
                   "as total from expenses_expense  as expense " \
                   "full Join  incomes_account as account " \
                   "ON expense.account_id = account.id " \
                   "where expense.user_profile_id = {0} and " \
                   "expense.created between '{1}-{2}-{3}' and '{4}-{5}-{6}' " \
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

        consulta = "select tipo_e.type as tipo," \
                   "sum(expense.value_expense) " \
                   "as total from expenses_expense as expense " \
                   "FULL JOIN expenses_typeexpense AS " \
                   "tipo_e ON expense.type_expense_id = " \
                   "tipo_e.id where expense.user_profile_id = {0} " \
                   "and expense.created between '{1}-{2}-{3}' " \
                   "and '{4}-{5}-{6}' group by tipo_e.type"
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
