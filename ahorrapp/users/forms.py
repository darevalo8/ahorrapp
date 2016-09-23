from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
