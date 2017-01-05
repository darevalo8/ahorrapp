from django import forms
from incomes.models import Account
# from expenses.models import TypeExpense
from .models import Obligation


class ObligationForm(forms.ModelForm):
    def get_selects(self, user_pro):
        self.fields['account'].queryset = Account.objects.filter(
            user_profile=user_pro)
        # self.fields['type_expense'].queryset = TypeExpense.objects.filter(
        #     user_profile=user_pro)

    class Meta:
        model = Obligation
        fields = (
            'name_obligation',
            'value_obligation',
            'end_obligation',
            'type_obligation',
            'account',
            'completed')
        widgets = {
            'end_obligation': forms.DateInput(attrs={'class': 'datepicker'}),
        }
