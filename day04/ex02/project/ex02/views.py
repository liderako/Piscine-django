from django.shortcuts import render
from django.http import HttpResponse
from .objects.MyForms import *
from django.conf import settings
from django import forms
import datetime
from django.utils import timezone

def     writeFile(data):
    fileObject = open(settings.LOG_FILE, "a")
    fileObject.write(data)
    fileObject.close()

def     readFile(nameFile):
    f = open(nameFile, 'r')
    res = f.read()
    return res.split('\n')

def     readBuffer():
    try:
        readBuffer = readFile(settings.LOG_FILE)
        return (readBuffer)
    except:
        readBuffer = []    
        return (readBuffer)

def     withForm(request):
    buffer = readBuffer()
    if (request.method == 'POST'):
        form = MyForms(request.POST)
        now = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
        if form.is_valid():
            data = form.cleaned_data['message'] + "\n"
            form.cleaned_data['message'] = ""
            writeFile(now + " " + data)
            buffer = readBuffer()
            return render(request, "forms.html", {'form' : form, 'messages' : buffer })
    else:
        form = MyForms()
    return render(request, "forms.html", {'form' : form, 'messages' : buffer })
