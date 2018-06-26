from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^init/$', views.index, name="index"),
    url(r'^init$', views.index, name="index"),
    url(r'^populate/$', views.populate),
    url(r'^populate$', views.populate),
    url(r'^display$', views.display),
    url(r'^display/$', views.display)
]