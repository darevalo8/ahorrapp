from django.utils import timezone
from django.db import models
from incomes.models import TimeStampedModel, Account
from expenses.models import TypeExpense
from users.models import UserProfile


class Obligation(TimeStampedModel):
    name_obligation = models.CharField(max_length=50)
    value_obligation = models.IntegerField()
    end_obligation = models.DateField(default=timezone.now)
    type_expense = models.ForeignKey(TypeExpense)
    user_profile = models.ForeignKey(UserProfile)
    account = models.ForeignKey(Account)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name_obligation
