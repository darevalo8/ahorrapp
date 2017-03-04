import calendar
import datetime
import json
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core import serializers
from django.views.generic import (View,
                                  CreateView,
                                  UpdateView)
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse


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
        date = self.get_star_and_end_date()
        context[self.context_object_name] = self.moodel.objects.filter(
            user_profile=request.user.userprofile.id,
            created__range=(date['start_date'], date['end_date']))
        return render(request, self.template_name, context)

    def get_star_and_end_date(self):
        current_date = timezone.now()
        max_day = max_days(current_date.year, current_date.month)
        start_date = datetime.date(current_date.year,
                                   current_date.month, 1)
        end_date = datetime.date(current_date.year,
                                 current_date.month, max_day[1])
        dates = {'start_date': start_date, 'end_date': end_date}

        return dates


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
        dates = self.get_star_and_end_date()
        object_list = self.moodel.objects.filter(
            user_profile=request.user.userprofile.id,
            created__range=(dates['start_date'], dates['end_date']))
        response = serializers.serialize("json", object_list, use_natural_keys=True)
        return HttpResponse(response, content_type='application/json')

    def get_date(self):
        date = {}
        if self.request.is_ajax():
            date['month'] = int(self.request.GET['mes'])
            date['year'] = int(self.request.GET['year'])
            return date
        else:
            return redirect('/')

    def get_star_and_end_date(self):
        date = self.get_date()
        max_day = max_days(date['year'], date['month'])
        start_date = datetime.date(date['year'], date['month'], 1)
        end_date = datetime.date(date['year'], date['month'], max_day[1])
        dates = {'start_date': start_date, 'end_date': end_date}
        return dates


def max_days(year, month):
    max_day = calendar.monthrange(year, month)
    return max_day


class TypeListView(BaseListView):

    def get(self, request):
        context = {}
        context[self.context_object_name] = self.moodel.objects.filter(
            user_profile=request.user.userprofile.id,)
        return render(request, self.template_name, context)


class BaseGroupAccount(BaseListView):
    def get(self, request):
        context = {}
        date = self.get_star_and_end_date()
        context[self.context_object_name] = self.moodel.objects.total_group_account(
            user_profile=request.user.userprofile.id,
            fecha_i=date['start_date'],
            fecha_f=date['end_date'])
        return render(request, self.template_name, context)


class AjaxGroupAccountView(AjaxListView):
    def get(self, request):
        dates = self.get_star_and_end_date()

        object_list = self.moodel.objects.total_group_account(
            user_profile=request.user.userprofile.id,
            fecha_i=dates['start_date'],
            fecha_f=dates['end_date'])
        # response = serializers.serialize("json", object_list)
        response = json.dumps(object_list)
        return HttpResponse(response, content_type='application/json')


class AjaxGroupTypeView(AjaxGroupAccountView):
    def get(self, request):
        dates = self.get_star_and_end_date()

        object_list = self.moodel.objects.total_group_type(
            user_profile=request.user.userprofile.id,
            fecha_i=dates['start_date'],
            fecha_f=dates['end_date'])
        # response = serializers.serialize("json", object_list)
        response = json.dumps(object_list)
        return HttpResponse(response, content_type='application/json')
