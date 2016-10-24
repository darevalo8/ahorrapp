from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.core.exceptions import PermissionDenied
from .models import UserProfile
from .viewmixins import LoginRequiredMixin


def dashboard(request):
    return render(request, 'users/dashboard.html', {})


class UserProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = 'detail_user'


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        # validamos que un usuario X no pueda actualizar un
        # perfil del usuario Y
        value_form = form.save(commit=False)
        slug = value_form.slug
        if self.request.user.userprofile.slug == slug:
            return super(UserProfileUpdate, self).form_valid(form)
        else:
            raise PermissionDenied
