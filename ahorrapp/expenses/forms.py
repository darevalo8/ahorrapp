from django import forms
from incomes.models import Account
from .models import (Expense, TypeExpense)


class ExpenseForm(forms.ModelForm):

    def get_selects(self, user_pro):
        self.fields['account'].queryset = Account.objects.filter(
            user_profile=user_pro)
        self.fields['type_expense'].queryset = TypeExpense.objects.filter(
            user_profile=user_pro)

    class Meta:
        model = Expense
        fields = (
            'name_expense',
            'value_expense',
            'account',
            'description',
            'type_expense')
