from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'admn'

urlpatterns = [
    url(r'^applications/$', views.applications, name='applications'),
]
