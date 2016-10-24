from django.conf.urls import url
from .views import (index,)
urlpatterns = [
    url(r'^lista/cuentas/$', index, name='index'),

]