from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^o-kompanii/$', views.company, name='company'),
    url(r'^sotrudniki/$', views.worker_list, name='worker_list'),
    url(r'^tehnika/$', views.machine_list, name='machine_list'),
    url(r'^prise/$', views.prise_list, name='prise_list'),



]