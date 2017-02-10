from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.log_in, name='login'),
    url(r'^logout/', views.log_out, name='logout'),
    url(r'^edit_profile/', views.edit_prof, name='edit_profile'),
    url(r'^change_password/$', views.change_pw, name='change_password_form'),
    url(r'^current_app/', views.current_app, name='current_app'),
   # url(r'^(?P<company_name>[\w\-]+)/$', views.company_details, name='company_details'),
    url(r'^(?P<company_id>[0-9]+)/$', views.company_details, name='company_details'),
    url(r'^register/$', views.apply, name='apply'),
    url(r'^apply/(?P<company_id>[0-9]+)/$', views.app_form, name='app_form'),

]