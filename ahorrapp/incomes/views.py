from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.views.generic import (View,)
from users.viewmixins import LoginRequiredMixin
from .models import (Account, TypeIncome, Income)
from .forms import IcomeForm
from .helpers import (BaseListView,
                      BaseCreateView,
                      BaseUpdateView,
                      AjaxDeleteView,
                      AjaxListView,
                      TypeListView)


class AccountCreateView(LoginRequiredMixin, BaseCreateView):
    model = Account
    fields = ['name_account', 'saldo_actual', 'account_type']
    success_url = reverse_lazy('incomes:list_account')


class AccountUpdateView(LoginRequiredMixin, BaseUpdateView):
    model = Account
    fields = ['name_account', 'saldo_actual', 'account_type']
    success_url = reverse_lazy('incomes:list_account')


class AccountDeleteView(LoginRequiredMixin, AjaxDeleteView):
    model = Account


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
            return redirect('incomes:list_income')


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
                raise PermissionDenied


class IncomeDeleteView(AccountDeleteView):
    model = Income


class TypeIncomeCreateView(AccountCreateView):
    model = TypeIncome
    fields = ['tipo']
    success_url = reverse_lazy('incomes:list_type')


class TypeIncomeListView(LoginRequiredMixin, TypeListView):
    moodel = TypeIncome
    template_name = 'incomes/typeincome_list.html'
    context_object_name = 'type_incomes'


class TypeIncomeUpdateView(AccountUpdateView):
    model = TypeIncome
    fields = ['tipo']
    success_url = reverse_lazy('incomes:list_type')


class TypeIncomeDeleteView(AccountDeleteView):
    model = TypeIncome


class IncomesAjaxList(AjaxListView):
    moodel = Income
