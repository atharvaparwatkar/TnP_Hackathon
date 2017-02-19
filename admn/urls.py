from django.conf.urls import url
from . import views

app_name = 'admn'

urlpatterns = [
    url(r'^$', views.admn_index, name="admnindex"),
    url(r'^login/$', views.admn_login, name="admnlogin"),
    url(r'^logout/$', views.admn_logout, name="admnlogout"),
    url(r'^companies/add$', views.add_company, name="add_companies"),
    url(r'^companies/(?P<company_id>[0-9]+)/$', views.edit_company, name="edit_companies"),
    url(r'^companies/$', views.companies, name="companies"),
    url(r'^users/$', views.users, name="users"),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.accept_user, name="acceptuser"),
    url(r'^users/(?P<user_id>[0-9]+)d/$', views.delete_user, name="deleteuser"),
    url(r'^users/(?P<user_id>[0-9]+)v/$', views.view_user, name="viewuser"),
    url(r'^users/(?P<user_id>[0-9]+)d2/$', views.delete_user2, name="deleteuserf"),
]
