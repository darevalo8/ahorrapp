from django import forms
from .models import (Income,
                     Account,
                     TypeIncome
                     )


class IcomeForm(forms.ModelForm):

    def get_selects(self, user_pro):
        self.fields['account'].queryset = Account.objects.filter(
            user_profile=user_pro)
        self.fields['type_income'].queryset = TypeIncome.objects.filter(
            user_profile=user_pro)

    class Meta:
        model = Income
        fields = (
            'nombre_ingreso',
            'valor_ingreso',
            'account',
            'description',
            'type_income')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }
