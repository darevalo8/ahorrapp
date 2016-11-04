from django.db import models


class SaldoFinalManager(models.Manager):
    use_for_related_fields = True

    def saldo_final(self, **kwargs):
        consulta = "select account.id, account.created, " \
                   "account.name_account, " \
                   "account.saldo_actual, account.user_profile_id, " \
                   "((account.saldo_actual - gastos)+ ingresos) " \
                   "as saldo_total " \
                   "from incomes_account as account FULL JOIN " \
                   "(select account_id, sum(valor_ingreso)as ingresos " \
                   "from incomes_income group by account_id) income " \
                   "ON income.account_id = account.id " \
                   "FULL JOIN (select account_id, sum(value_expense) " \
                   "as gastos from expenses_expense group by account_id) " \
                   "expense ON expense.account_id = account.id " \
                   "where account.user_profile_id = {0};"
        return self.raw(consulta.format(kwargs['user_id']))
