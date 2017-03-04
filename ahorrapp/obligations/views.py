from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from incomes.helpers import (BaseListView,
                             AjaxDeleteView,
                             AjaxListView)
from .forms import ObligationForm
from .models import Obligation
from users.viewmixins import LoginRequiredMixin


class ObligationCreateView(LoginRequiredMixin, View):
    template_name = 'obligations/obligation_form.html'

    def get(self, request):
        form_class = ObligationForm()
        form_class.get_selects(request.user.userprofile.id)
        return render(request, self.template_name, {'form': form_class})

    @staticmethod
    def post(request):
        form_class = ObligationForm(request.POST)
        if form_class.is_valid():
            obligation = form_class.save(commit=False)
            obligation.user_profile_id = request.user.userprofile.id
            obligation.save()
            return redirect('obligations:list_obligation')


class ObligationListView(LoginRequiredMixin, BaseListView):
    moodel = Obligation
    template_name = 'obligations/obligation_list.html'
    context_object_name = 'obligations'


class ObligationUpdateView(LoginRequiredMixin, View):
    template_name = 'obligations/obligation_form.html'

    def get(self, request, pk):
        obligation_object = Obligation.objects.get(pk=pk)
        if obligation_object.user_profile_id == request.user.userprofile.id:
            form_class = ObligationForm(instance=obligation_object)
            form_class.get_selects(request.user.userprofile.id)
        else:
            raise Http404
        return render(request, self.template_name, {'form': form_class})

    @staticmethod
    def post(request, pk):
        obligation_object = Obligation.objects.get(pk=pk)
        form = ObligationForm(request.POST, instance=obligation_object)
        if form.is_valid():
            obligation_value = form.save(commit=False)
            if obligation_value.user_profile_id == request.user.userprofile.id:
                obligation_value.save()
                return redirect('obligations:list_obligation')
            else:
                raise PermissionDenied


class ObligationDeleteView(LoginRequiredMixin, AjaxDeleteView):
    model = Obligation
    template_name = 'obligations/obligation_delete.html'
    success_url = reverse_lazy('obligations:list_obligation')


class ObligationAjaxListView(LoginRequiredMixin, AjaxListView):
    moodel = Obligation
