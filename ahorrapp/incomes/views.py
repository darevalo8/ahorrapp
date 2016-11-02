from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
from django.views.generic import (View,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from users.viewmixins import LoginRequiredMixin
from .models import (Account, TypeIncome, Income)
from .forms import IcomeForm
from .helpers import BaseListView


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    fields = ['name_account', 'saldo_actual']
    success_url = reverse_lazy('incomes:list_account')

    def form_valid(self, form):
        form_value = form.save(commit=False)
        form_value.user_profile_id = self.request.user.userprofile.id
        form_value.save()
        return super(AccountCreateView, self).form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
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


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = reverse_lazy('incomes:list_account')
    template_name = 'incomes/account_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user_profile_id == request.user.userprofile.id:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            raise Http404

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        success_url = self.get_success_url()

        if self.object.user_profile_id == request.user.userprofile.id:
            self.object.delete()
        else:
            raise PermissionDenied
        return HttpResponseRedirect(success_url)


class AccountListView(LoginRequiredMixin, View):
    template_name = 'incomes/account_list.html'

    def get(self, request):

        accounts = Account.objects.saldo_final(
            user_id=request.user.userprofile.id)
        return render(request, self.template_name, {'accounts': accounts})


class CreateIncome(LoginRequiredMixin, View):
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


class IncomeListView(LoginRequiredMixin, BaseListView):
    moodel = Income
    context_object_name = 'incomes'
    template_name = 'incomes/income_list.html'


class IncomeUpdateView(LoginRequiredMixin, View):
    template_name = 'incomes/income_form.html'

    def get(self, request, pk):
        income_object = Income.objects.get(pk=pk)
        if income_object.user_profile_id == request.user.userprofile.id:
            form_class = IcomeForm(instance=income_object)
            form_class.get_selects(request.user.userprofile.id)
        else:
            raise Http404
        return render(request, self.template_name, {'form': form_class})

    @staticmethod
    def post(request, pk):
        income_object = Income.objects.get(pk=pk)
        form = IcomeForm(request.POST, instance=income_object)
        if form.is_valid():
            income_value = form.save(commit=False)
            if income_value.user_profile_id == request.user.userprofile.id:
                income_value.save()
                return redirect('incomes:list_income')
            else:
                raise Http404


class IncomeDeleteView(AccountDeleteView):
    model = Income
    template_name = 'incomes/income_delete.html'
    success_url = reverse_lazy('incomes:list_income')


class TypeIncomeCreateView(AccountCreateView):
    model = TypeIncome
    fields = ['tipo']
    success_url = reverse_lazy('incomes:list_type')


class TypeIncomeListView(LoginRequiredMixin, BaseListView):
    moodel = TypeIncome
    template_name = 'incomes/typeincome_list.html'
    context_object_name = 'type_incomes'


class TypeIncomeUpdateView(AccountUpdateView):
    model = TypeIncome
    fields = ['tipo']
    success_url = reverse_lazy('incomes:list_type')


class TypeIncomeDeleteView(AccountDeleteView):
    model = TypeIncome
    success_url = reverse_lazy('incomes:list_type')
    template_name = 'incomes/typeincome_delete.html'
