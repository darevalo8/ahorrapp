from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.core.exceptions import PermissionDenied
from .models import UserProfile
from .viewmixins import LoginRequiredMixin
# from .forms import UserForm


def dashboard(request):
    return render(request, 'users/dashboard.html', {})


# class UserProfileCreateView(CreateView):
#     """
#     en esta clase vamos a registrar los usuarios
#     """
#     form_class = UserForm
#     model = UserProfile
#
#     def form_valid(self, form):
#         """
#         en este metodo lo que vamos hacer es encriptar la contraseña de los usuarios cuando se registran
#         """
#         user_profile = form.save(commit=False)
#         user_profile.set_password(user_profile.password)
#         user_profile.save()
#
#         return super(UserProfileCreateView, self).form_valid(form)


class UserProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = 'detail_user'


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        value_form = form.save(commit=False)
        slug = value_form.slug
        print(slug)
        print(self.request.user.userprofile.slug)
        if self.request.user.userprofile.slug == slug:
            return super(UserProfileUpdate, self).form_valid(form)
        else:
            raise PermissionDenied
