from django.db import models
from users.models import UserProfile
from incomes.models import TimeStampedModel, Account


class TypeExpense(models.Model):
    type = models.CharField(max_length=50)
    user_profile = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.type


class Expense(TimeStampedModel):
    name_expense = models.CharField(max_length=50)
    value_expense = models.IntegerField()
    description = models.TextField(max_length=150, blank=True)
    type_expense = models.ForeignKey(TypeExpense)
    user_profile = models.ForeignKey(UserProfile)
    account = models.ForeignKey(Account)

    def __str__(self):
        return self.name_expense
