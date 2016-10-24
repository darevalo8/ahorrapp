from django.shortcuts import render
from .models import Account


def index(request):
    print(type(request.user.userprofile.id))
    account = Account.objects.saldo_final()
    return render(request, 'incomes/index.html', {'accounts': account})
