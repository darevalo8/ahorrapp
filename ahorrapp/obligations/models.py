from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator
from incomes.models import TimeStampedModel, Account
from users.models import UserProfile


class ObligationManager(models.Manager):
    def get_by_natural_key(self, tipo):
        return self.get(type_obligation=tipo)


class Obligation(TimeStampedModel):
    choice_obligation = (
        (1, 'Educacion'),
        (2, 'Hogar'),
        (3, 'Creditos'),
        (4, 'Otros')
    )
    name_obligation = models.CharField(max_length=50)
    value_obligation = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    end_obligation = models.DateField(default=timezone.now)
    type_obligation = models.IntegerField(choices=choice_obligation, default=4)
    user_profile = models.ForeignKey(UserProfile)
    account = models.ForeignKey(Account)
    completed = models.BooleanField(default=False)
    objects = ObligationManager()

    def natural_key(self):
        return self.type_obligation

    def __str__(self):
        return self.name_obligation
