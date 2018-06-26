from django.conf.urls import url
from . import views
from django.http import HttpResponse

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^$', views.index, name="index")
]