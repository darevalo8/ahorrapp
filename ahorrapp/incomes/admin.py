from django.contrib import admin
from .models import (Account, Income, TypeIncome)

admin.site.register(Account)
admin.site.register(Income)
admin.site.register(TypeIncome)
