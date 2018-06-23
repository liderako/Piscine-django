from django.conf.urls import url
from . import views
from django.http import HttpResponse

urlpatterns = [
    # url(r'^withForm$', views.withForm, name="withform"),
    # url(r'^withForm/$', views.withForm, name="withform"),
    url(r'^$', views.withForm),
]