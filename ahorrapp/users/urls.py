from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import (dashboard, UserProfileDetailView, UserProfileUpdate)

urlpatterns = [
    url(r'^dashboard$', dashboard, name='dashboard'),
    # url(r'^register$', UserProfileCreateView.as_view(), name='register_user'),
    # url(r'^login$', auth_views.login,
    #     {'template_name': 'registration/login.html'},
    #     name='login'),
    url(r'^logout$', auth_views.logout,
        {'template_name': 'registration/logout.html'},
        name='logout'),
    url(
        r'^password/change/$',
        auth_views.password_change,
        {
            'post_change_redirect': reverse_lazy('auth_password_change_done')
        },
        name='auth_password_change'
    ),
    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='auth_password_change_done'),
    url(r'^password/reset/$',
        auth_views.password_reset,
        {'post_reset_redirect': reverse_lazy('auth_password_reset_done')},
        name='auth_password_reset'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='auth_password_reset_complete'),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='auth_password_reset_done'),

    url(r'^detail/(?P<slug>[-\w]+)/$', UserProfileDetailView.as_view(), name='user_detail'),
    url(r'^update/(?P<slug>[-\w]+)/$', UserProfileUpdate.as_view(), name='update_user')
]
