from django.shortcuts import render
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
        context[self.context_object_name] = self.moodel.objects.filter(
            user_profile=request.user.userprofile.id)
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

# class CreateIncome(View):
#     """
#     el que vaya a  usar este helper, se tiene que crear
#     el metodo get_selects en su form class
#     """
#
#     template_name = ''
#     form_class = None
#     succes_url = None
#
#     def get(self, request):
#         form_instance = self.form_class()
#         form_instance.get_selects(request.user.userprofile.id)
#         return render(request, self.template_name, {'form': form_instance})
#
#     def post(self, request):
#         form_instance = self.form_class()
#         if form_instance.is_valid():
#             income = form_instance.save(commit=False)
#             income.user_profile_id = request.user.userprofile.id
#             income.save()
#             return redirect('expenses:list_expense')
#
#     def get_succes_url(self):
#         url = ''
#         if self.succes_url:
#             url = force_text(self.succes_url)
#             print(url)
#         return url
