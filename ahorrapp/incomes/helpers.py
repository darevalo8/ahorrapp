from django.shortcuts import render
from django.views.generic import (View,)


class BaseListView(View):
    """
    este helper siver para hacer un
    filtro de un objecto asoiciado al usuario logueado
    """
    template_name = ''
    moodel = None
    context_object_name = ''

    def get(self, request):
        context = {}
        context[self.context_object_name] = self.moodel.objects.filter(
            user_profile=request.user.userprofile.id)
        return render(request, self.template_name, context)
