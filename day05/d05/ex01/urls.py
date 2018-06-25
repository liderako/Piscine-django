from django.conf.urls import url
from . import views
from django.http import HttpResponse

urlpatterns = [
    url(r'^init/$', views.index, name="index"),
    url(r'^init$', views.index, name="index")
]