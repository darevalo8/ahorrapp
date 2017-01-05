from django.db import models
from django.core.validators import MaxValueValidator
from users.models import UserProfile
from .managers import AccountManager, TypeIncomeManager


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Account(TimeStampedModel):
    objects = AccountManager()
    choices_account = (
        (1, 'Efectivo'),
        (2, 'Ahorros'),
        (3, 'Inversiones'),
        (4, 'Otros')
    )
    name_account = models.CharField(max_length=50)
    saldo_actual = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    user_profile = models.ForeignKey(UserProfile)
    account_type = models.IntegerField(choices=choices_account, default=1)
    
    def __str__(self):
        return self.name_account

    def natural_key(self):
        return self.name_account

    # class Meta:
    #     unique_together = (('name_account',),)


class TypeIncome(models.Model):
    tipo = models.CharField(max_length=50)
    user_profile = models.ForeignKey(UserProfile)
    objects = TypeIncomeManager()

    def natural_key(self):
        return self.tipo

    def __str__(self):
        return self.tipo


class Income(TimeStampedModel):
    nombre_ingreso = models.CharField(max_length=50)
    valor_ingreso = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    account = models.ForeignKey(Account)
    description = models.TextField(max_length=100, blank=True)
    user_profile = models.ForeignKey(UserProfile)
    type_income = models.ForeignKey(TypeIncome)

    def __str__(self):
        return self.nombre_ingreso
