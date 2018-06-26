from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from .forms import *

def     withForm(request):
    data = ""
    if (request.method == 'POST'):
        form = removeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['title']
    else:
        form = removeForm()
    return form, data

def populate(req):
    l = [
        ['1', 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'],
        ['2', 'Attack of the Clones', 'George Lucas', 'Rick McCallum','2002-05-16'],
        ['3', 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'],
        ['4', 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum','1977-05-25'],
        ['5', 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum','1980-05-17'],
        ['6', 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum','1983-05-25'],
        ['7', 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk','2015-12-11']
    ]
    res = ""
    i = 0
    for x in l:
        m = Movies(
            title=x[1],
            director=x[2],
            producer=x[3],
            episode_nb=x[0],
            release_date=x[4],
        )
        i += 1
        try:
            m.save()
            res += " OK " + str(i)
        except Exception as e:
            return (HttpResponse("KO " + str(i) + str(e)))
    return (HttpResponse(res))

def display(requests):
    try:
        res = Movies.objects.all()
        l = list()
        if (len(res) == 0):
            raise Exception("len < 0")
        for x in res:
            l.append([x.episode_nb, x.title, x.director, x.producer, x.opening_crawl or None, x.release_date])
        return render(requests, "ex05/display.html", {'data': l})
    except Exception as e:
        return (HttpResponse("No data available"))

def remove(requests):
    form, data = withForm(requests)
    res = Movies.objects.all()
    l = list()
    id = None
    for x in res:
        if (x.title == data):
            id = x.episode_nb
            break
    if (id != None):
        tmpR = Movies.objects.get(episode_nb=id)
        tmpR.delete()

    res = Movies.objects.all()
    for x in res:
        l.append(x.title)
    return render(requests, "ex05/remove.html", {'data': l, 'form' : form})