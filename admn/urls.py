from django.conf.urls import url
from . import views

app_name = 'admn'

urlpatterns = [
    url(r'^companies/add$', views.add_company, name="add_companies"),
    url(r'^companies/(?P<company_id>[0-9]+)/$', views.edit_company, name="edit_companies"),
    url(r'^companies/$', views.companies, name="companies"),
    url(r'^users/$', views.users, name="users"),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.accept_user, name="acceptuser"),
]
