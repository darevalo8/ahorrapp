from django import forms

from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password',)
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'validate',
                'id': 'password'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'validate',
                'id': 'email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'validate',
                'id': 'username'
            })
        }



