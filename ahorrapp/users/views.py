from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse
from .models import UserProfile
from .forms import UserForm


def dashboard(request):
    return render(request, 'users/dashboard.html', {})


class UserProfileCreateView(CreateView):
    """
    en esta clase vamos a registrar los usuarios
    """
    form_class = UserForm
    model = UserProfile

    def form_valid(self, form):
        """
        en este metodo lo que vamos hacer es encriptar la contraseña de los usuarios cuando se registran
        """
        user_profile = form.save(commit=False)
        user_profile.set_password(user_profile.password)
        user_profile.save()

        return super(UserProfileCreateView, self).form_valid(form)
