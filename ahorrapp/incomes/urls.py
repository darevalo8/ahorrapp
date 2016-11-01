from django.conf.urls import url
from .views import (AccountListView,
                    AccountCreateView,
                    CreateIncome,
                    TypeIncomeCreateView,
                    TypeIncomeListView,
                    AccountUpdateView,
                    AccountDeleteView
                    )
urlpatterns = [
    url(r'^lista/cuentas/$', AccountListView.as_view(), name='list_account'),
    url(r'^create/cuentas/$', AccountCreateView.as_view(), name='create_account'),
    url(r'^update/cuenta/(?P<pk>\d+)/$',AccountUpdateView.as_view(), name='update_account'),
    url(r'^delete/cuenta/(?P<pk>\d+)/$',AccountDeleteView.as_view(), name='delete_account'),
    url(r'^create/ingreso/$', CreateIncome.as_view(), name='create_income'),
    url(r'^create/type/$', TypeIncomeCreateView.as_view(), name='create_type'),
    url(r'^list/type/$', TypeIncomeListView.as_view(), name='list_type'),

]
