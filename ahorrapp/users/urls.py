from django.conf.urls import url
from django.contrib.auth import views
from .views import (index, UserProfileCreateView)

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^register$', UserProfileCreateView.as_view(), name='register_user'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, {'next_page': 'users:home'}, name='logout'),
    url(r'^password-reset$',
        views.password_reset,
        {
            'post_reset_redirect': 'users:reset_done',
            'from_email': 'danielfelipe.arevalo2@gmail.com'
        },
        name='recordar_contraseña'),
    url(r'^password-reset-done$', views.password_reset_done, name='reset_done'),
    url(r'^password-reset-confirm', views.password_reset_confirm, name='reset_confirm'),
]
