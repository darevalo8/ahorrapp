from django.conf.urls import include, url
from .views import Dashboard
urlpatterns = [
    url(r'^$', Dashboard.as_view(), name='index'),
    # url(r'^cuentas/', include('incomes.urls', namespace='incomes')),

]