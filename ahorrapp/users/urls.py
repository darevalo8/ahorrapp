from django.conf.urls import url
from django.contrib.auth import views
from .views import (dashboard, UserProfileCreateView)

urlpatterns = [
    url(r'^dashboard$', dashboard, name='dashboard'),
    url(r'^register$', UserProfileCreateView.as_view(), name='register_user'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, {'next_page': 'landing'}, name='logout'),
    url(
        r'^password-change/$',
        views.password_change,
        {
            'post_change_redirect': 'users:password_change_done'
        },
        name='password_change'
    ),
    url(r'^password-change-done/', views.password_change_done, name='password_change_done'),
    url(
        r'^password-reset$',
        views.password_reset,
        {
            'post_reset_redirect': 'users:reset_done',
            # 'from_email': 'danielfelipe.arevalo2@gmail.com'
        },
        name='recordar_contraseña'),
    url(r'^password-reset-done$', views.password_reset_done, name='reset_done'),
    url(
        r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm,
        {
            'post_reset_redirect': 'users:reset_complete'
        },
        name='reset_confirm'),
    url(r'^password-reset-complete$', views.password_reset_complete, name='reset_complete'),
]
