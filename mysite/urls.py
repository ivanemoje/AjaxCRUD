from django.conf.urls import url, include
from django.views.generic import TemplateView

from mysite.clients import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^clients/$', views.client_list, name='client_list'),
    url(r'^clients/create/$', views.client_create, name='client_create'),
    url(r'^clients/(?P<pk>\d+)/update/$', views.client_update, name='client_update'),
    url(r'^clients/(?P<pk>\d+)/delete/$', views.client_delete, name='client_delete'),
]
