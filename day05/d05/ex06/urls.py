from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^init/$', views.init),
    url(r'^init$', views.init),
    url(r'^display$', views.display),
    url(r'^display/$', views.display),
    url(r'^populate/$', views.populate),
    url(r'^populate$', views.populate),
    url(r'^update$', views.update),
    url(r'^update/$', views.update),
]