from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # a = "This is a template."
    # return render(request, "ex00/index.html", locals())

def index(request):
    return render(request, "ex00/index.html")

# def withtemplate(request):
	# return HttpResponse("Template")
	# return render(request, "ex00/index.html")

