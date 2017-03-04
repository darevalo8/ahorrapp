from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.http import Http404
from django.core.exceptions import PermissionDenied
from incomes.helpers import (BaseCreateView,
                             BaseListView,
                             BaseUpdateView,
                             AjaxDeleteView,
                             TypeListView,
                             AjaxListView,
                             AjaxGroupAccountView,
                             AjaxGroupTypeView,
                             BaseGroupAccount)
from users.viewmixins import LoginRequiredMixin
from .models import TypeExpense, Expense
from .forms import ExpenseForm


class TypeExpenseListView(LoginRequiredMixin, TypeListView):
    moodel = TypeExpense
    template_name = 'expenses/typeexpense_list.html'
    context_object_name = 'type_expenses'


class TypeExpenseCreateView(LoginRequiredMixin, BaseCreateView):
    model = TypeExpense
    fields = ['type']
    success_url = reverse_lazy('expenses:list_typeexpense')


class TypeExpenseUpdateView(LoginRequiredMixin, BaseUpdateView):
    model = TypeExpense
    fields = ['type']
    success_url = reverse_lazy('expenses:list_typeexpense')


class TypeExpenseDeleteView(LoginRequiredMixin, AjaxDeleteView):
    model = TypeExpense


class ExpenseCreateView(LoginRequiredMixin, View):
    template_name = 'expenses/expense_form.html'

    def get(self, request):
        form_class = ExpenseForm()
        form_class.get_selects(request.user.userprofile.id)
        return render(request, self.template_name, {'form': form_class})

    @staticmethod
    def post(request):
        form_class = ExpenseForm(request.POST)
        if form_class.is_valid():
            income = form_class.save(commit=False)
            income.user_profile_id = request.user.userprofile.id
            income.save()
            return redirect('expenses:list_expense')


class ExpenseUpdateView(LoginRequiredMixin, View):
    template_name = 'expenses/expense_form.html'

    def get(self, request, pk):
        income_object = Expense.objects.get(pk=pk)
        if income_object.user_profile_id == request.user.userprofile.id:
            form_class = ExpenseForm(instance=income_object)
            form_class.get_selects(request.user.userprofile.id)
        else:
            raise Http404
        return render(request, self.template_name, {'form': form_class})

    @staticmethod
    def post(request, pk):
        income_object = Expense.objects.get(pk=pk)
        form = ExpenseForm(request.POST, instance=income_object)
        if form.is_valid():
            income_value = form.save(commit=False)
            if income_value.user_profile_id == request.user.userprofile.id:
                income_value.save()
                return redirect('expenses:list_expense')
            else:
                raise PermissionDenied


class ExpenseListView(LoginRequiredMixin, BaseListView):
    moodel = Expense
    template_name = 'expenses/expense_list.html'
    context_object_name = 'expenses'


class ExpenseDeleteView(TypeExpenseDeleteView):
    model = Expense


class ExpenseAjaxList(LoginRequiredMixin, AjaxListView):
    moodel = Expense


class ExpenseGroupView(LoginRequiredMixin, BaseGroupAccount):
    moodel = Expense
    template_name = 'expenses/expense_group.html'
    context_object_name = 'grupos'


class ExpenseGroupAccountView(LoginRequiredMixin,
                              AjaxGroupAccountView):
    moodel = Expense


class ExpenseGroupTypeView(LoginRequiredMixin,
                           AjaxGroupTypeView):
    moodel = Expense
