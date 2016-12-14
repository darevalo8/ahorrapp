"""ahorrapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .index import landing

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^cuentas/', include('incomes.urls', namespace='incomes')),
    url(r'^expenses/', include('expenses.urls', namespace='expenses')),
    url(r'^obligations/', include('obligations.urls', namespace='obligations')),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^$', landing, name='landing'),

]
