from django.shortcuts import render
from django.http import HttpResponse
from .objects.MyForms import *
from django.conf import settings
from django import forms

def     index(request):
    return HttpResponse("Here's the text of the Web page.")

def     withForm(request):
    if (request.method == 'POST'):
        form = MyForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data['message'] + "\n"
            fileObject = open(settings.LOG_FILE, "a")
            fileObject.write(data)
            fileObject.close()
            return render(request, "forms.html", {'form' : form, 'message' : data})
    else:
        form = MyForms()
    return render(request, "forms.html", {'form' : form, "message" : "test"})
