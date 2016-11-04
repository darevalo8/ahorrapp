from django.test import TestCase
from users.models import UserProfile
from expenses.models import TypeExpense, Expense
from .models import Account, Income, TypeIncome


class AccountTest(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create_user(
            username='darevalo8',
            email='darevalo08@hotmail.com',
            password='12345678')
        self.account1 = Account.objects.create(
            name_account='account1',
            saldo_actual='20000',
            user_profile=self.user)
        self.account2 = Account.objects.create(
            name_account='account2',
            saldo_actual='15000',
            user_profile=self.user)
        self.type = TypeIncome.objects.create(tipo='salario',
                                              user_profile=self.user)
        self.type_expense = TypeExpense.objects.create(type='comida',
                                                       user_profile=self.user)

        Expense.objects.create(name_expense='holi',
                               value_expense=2000,
                               description='holdsaklds',
                               type_expense=self.type_expense,
                               user_profile=self.user,
                               account=self.account1)
        Income.objects.create(
            nombre_ingreso='nombre_account1', valor_ingreso=1000,
            account=self.account1,
            user_profile=self.user,
            type_income=self.type)

    def test_saldo_final(self):
        print(Account.objects.saldo_final(user_id=self.user.id)[0])
        self.assertEqual(Account.objects.saldo_final(
            user_id=self.user.id)[0].saldo_total, 19000)
        self.assertEqual(Account.objects.saldo_final(
            user_id=self.user.id)[1].saldo_actual, 15000)
