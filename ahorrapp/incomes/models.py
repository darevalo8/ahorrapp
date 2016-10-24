from django.db import models


class SaldoFinalManager(models.Manager):
    use_for_related_fields = True

    def saldo_final(self, **kwargs):
        consulta = "select account.id,account.name_account,  " \
                   "sum(income.valor_ingreso)+account.saldo_actual as " \
                   "saldo_actual,account.created " \
                   "from incomes_income as income " \
                   "inner join incomes_account as " \
                   "account on income.account_id = account.id " \
                   "group by account.saldo_actual, account.name_account," \
                   " account.id, account.created;"
        return self.raw(consulta)


class Account(models.Model):
    name_account = models.CharField(max_length=50)
    saldo_actual = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = SaldoFinalManager()

    def __str__(self):
        return self.name_account


class Income(models.Model):
    nombre_ingreso = models.CharField(max_length=50)
    valor_ingreso = models.IntegerField()
    description = models.TextField(max_length=3000)
    account = models.ForeignKey(Account)

    def __str__(self):
        return self.nombre_ingreso
