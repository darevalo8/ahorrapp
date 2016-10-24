from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import UserProfile


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('username', 'email', 'password',)
#         widgets = {
#             'password': forms.PasswordInput(attrs={
#                 'class': 'validate',
#                 'id': 'password'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'validate',
#                 'id': 'email'
#             }),
#             'username': forms.TextInput(attrs={
#                 'class': 'validate',
#                 'id': 'username'
#             })
#         }


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')
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

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if UserProfile.objects.filter(
                email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(
                _("This email address is already in use. "
                  " Please supply a different email address."))
        return self.cleaned_data['email']

    def save(self, commit=True):
        """editamos este metodo para que cuando vaya a guardar
        un usuario encripte la contraseña"""
        user = super(UserProfileForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
