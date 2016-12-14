from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.core.exceptions import PermissionDenied
from django.http import Http404
from .models import UserProfile
from .viewmixins import LoginRequiredMixin


# def dashboard(request):
#     return render(request, 'users/dashboard.html', {})


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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # validamos si el usuario que va actualizar
        # es el dueño de la cuenta si no lo es
        # mandamos un Httpe404
        if self.object.id == request.user.userprofile.id:
            form = self.get_form()
        else:
            raise Http404

        return self.render_to_response(self.get_context_data(form=form))