from django.conf.urls import url
from .views import (ObligationListView,
                    ObligationCreateView,
                    ObligationUpdateView,
                    ObligationDeleteView)

urlpatterns = [
    url(r'^create/$', ObligationCreateView.as_view(), name='create_obligation'),
    url(r'^list/$', ObligationListView.as_view(), name='list_obligation'),
    url(r'^update/(?P<pk>\d+)/$', ObligationUpdateView.as_view(), name='update_obligation'),
    url(r'^delete/(?P<pk>\d+)/$', ObligationDeleteView.as_view(), name='delete_obligation'),

]
