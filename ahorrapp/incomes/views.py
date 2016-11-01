from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
from django.views.generic import (View,
                                  CreateView,
                                  UpdateView, DeleteView)
from .models import (Account, TypeIncome)
from .forms import IcomeForm


class AccountCreateView(CreateView):
    model = Account
    fields = ['name_account', 'saldo_actual']
    success_url = reverse_lazy('incomes:list_account')

    def form_valid(self, form):
        form_value = form.save(commit=False)
        form_value.user_profile_id = self.request.user.userprofile.id
        form_value.save()
        return super(AccountCreateView, self).form_valid(form)


class AccountUpdateView(UpdateView):
    model = Account
    fields = ['name_account', 'saldo_actual']
    success_url = reverse_lazy('incomes:list_account')

    def form_valid(self, form):
        form_value = form.save(commit=False)
        # validamos que un usuario X no pueda actualizar una
        # cuenta de un usuario Y
        if self.request.user.userprofile.id == form_value.user_profile_id:
            form_value.save()
        else:
            raise PermissionDenied
        return super(AccountUpdateView, self).form_valid(form)

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


class AccountDeleteView(DeleteView):
    model = Account
    success_url = reverse_lazy('incomes:list_account')
    template_name = 'incomes/account_delete.html'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        success_url = self.get_success_url()

        if self.object.user_profile_id == request.user.userprofile.id:
            self.object.delete()
        else:
            raise PermissionDenied
        return HttpResponseRedirect(success_url)


class AccountListView(View):
    template_name = 'incomes/account_list.html'

    def get(self, request):

        accounts = Account.objects.saldo_final(user_id=request.user.userprofile.id)
        return render(request, self.template_name, {'accounts': accounts})


class CreateIncome(View):
    template_name = 'incomes/income_form.html'

    def get(self, request):
        form_class = IcomeForm()
        form_class.get_selects(request.user.userprofile.id)
        return render(request, self.template_name, {'form': form_class})

    @staticmethod
    def post(request):
        form_class = IcomeForm(request.POST)
        if form_class.is_valid():
            income = form_class.save(commit=False)
            income.user_profile_id = request.user.userprofile.id
            income.save()
            return redirect('incomes:list_account')


class IncomeUpdateView(View):
    pass


class TypeIncomeCreateView(AccountCreateView):
    model = TypeIncome
    fields = ['tipo']
    success_url = reverse_lazy('incomes:list_type')


class TypeIncomeListView(View):
    type_incomes = None

    def get(self, request):
        context = {'type_incomes': None, 'menssage': ''}
        self.type_incomes = TypeIncome.objects.filter(user_profile=request.user.userprofile.id)
        if self.type_incomes:
            context['type_incomes'] = self.type_incomes
        else:
            context['menssage'] = 'No hay registros'
        return render(request, 'incomes/typeincome_list.html', context)
