from django.db import models
from users.models import UserProfile
from .managers import SaldoFinalManager


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(TimeStampedModel):
    choices_account = (
        (1, 'Dinero'),
        (2, 'Ahorros'),
        (3, 'Inversiones'),
        (4, 'Salario'),
        (5, 'Otros')
    )
    name_account = models.CharField(max_length=50)
    saldo_actual = models.IntegerField(max_length=15)
    user_profile = models.ForeignKey(UserProfile)
    account_type = models.IntegerField(choices=choices_account, default=1)
    objects = SaldoFinalManager()

    def __str__(self):
        return self.name_account


class TypeIncome(models.Model):
    tipo = models.CharField(max_length=50)
    user_profile = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.tipo


class Income(TimeStampedModel):
    nombre_ingreso = models.CharField(max_length=50)
    valor_ingreso = models.IntegerField()
    account = models.ForeignKey(Account)
    description = models.TextField(max_length=100, blank=True)
    user_profile = models.ForeignKey(UserProfile)
    type_income = models.ForeignKey(TypeIncome)

    def __str__(self):
        return self.nombre_ingreso
