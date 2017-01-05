import calendar
import datetime
import json
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core import serializers
from django.views.generic import (View,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect, HttpResponse


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
        current_date = timezone.now()
        max_day = max_days(current_date.year, current_date.month)
        start_date = datetime.date(current_date.year,
                                   current_date.month, 1)
        end_date = datetime.date(current_date.year,
                                 current_date.month, max_day[1])
        context[self.context_object_name] = self.moodel.objects.filter(
            user_profile=request.user.userprofile.id,
            created__range=(start_date, end_date))
        return render(request, self.template_name, context)


class BaseCreateView(CreateView):
    """
    esta clase hereda de create view y modifica el
    metodo form_valid para asi guardar los datos
    del usuario que esta logueado
    """
    def form_valid(self, form):
        form_value = form.save(commit=False)
        form_value.user_profile_id = self.request.user.userprofile.id
        form_value.save()
        return super(BaseCreateView, self).form_valid(form)


class BaseUpdateView(UpdateView):
    """
    en esta clase modificamos el metodo form_valid
    para que solo el usuario dueño de su registro lo
    pueda modificar, y si es otro usuario
    le da permiso denegado y en el metodo
    get le retorna un error 404
    """
    def form_valid(self, form):
        form_value = form.save(commit=False)
        # validamos que un usuario X no pueda actualizar una
        # cuenta de un usuario Y
        if self.request.user.userprofile.id == form_value.user_profile_id:
            form_value.save()
        else:
            raise PermissionDenied
        return super(BaseUpdateView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # validamos si el usuario que va actualizar
        # es el dueño de la cuenta si no
        # le mandamos none
        if self.object.user_profile_id == request.user.userprofile.id:
            form = self.get_form()
        else:
            raise Http404

        return self.render_to_response(self.get_context_data(form=form))


class BaseDeleteView(DeleteView):
    """
    esta clase funciona igual que la clase
    BaseUpdate view, lo que cambia que
    esta clase es para hacer una eliminacion
    de registros
    """
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user_profile_id == request.user.userprofile.id:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            raise Http404

    def delete(self, request, *args, **kwargs):
        if self.request.is_ajax():
            print("holaaaa")
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.object.user_profile_id == request.user.userprofile.id:
            self.object.delete()
        else:
            raise PermissionDenied
        return HttpResponseRedirect(success_url)


class AjaxDeleteView(View):
    model = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        if self.request.is_ajax():
            print('account pk = {0}'.format(pk))
            if obj.user_profile_id == request.user.userprofile.id:
                obj.delete()
                return HttpResponse('Eliminado')
            else:
                raise Http404
        else:
            raise Http404


class AjaxListView(BaseListView):

    def get(self, request):
        date = self.get_date()
        max_day = max_days(date['year'], date['month'])
        start_date = datetime.date(date['year'], date['month'], 1)
        end_date = datetime.date(date['year'], date['month'], max_day[1])
        object_list = self.moodel.objects.filter(
            user_profile=request.user.userprofile.id,
            created__range=(start_date, end_date))
        # listado = [{'nombre_ingreso': obj.nombre_ingreso} for obj in objeto]
        # response = json.dumps(listado)
        response = serializers.serialize("json", object_list, use_natural_keys=True)
        return HttpResponse(response, content_type="application/json")

    def get_date(self):
        date = {}
        if self.request.is_ajax():
            date['month'] = int(self.request.GET['mes'])
            date['year'] = int(self.request.GET['year'])
            return date
        else:
            return redirect('/')


def max_days(year, month):
    max_day = calendar.monthrange(year, month)
    print("hola")
    return max_day


class TypeListView(BaseListView):

    def get(self, request):
        context = {}
        context[self.context_object_name] = self.moodel.objects.filter(
            user_profile=request.user.userprofile.id,)
        return render(request, self.template_name, context)
