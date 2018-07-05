from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import os
import random
from .api import Data
from .object.DataStorage import DataStorage
from .load_view import *

GD = DataStorage()

def     index(request):
    settings.INDEX = 0
    if request.method == "GET":
        button = request.GET.get('button')
        if button:
            if (button == "A"):
                d = DataStorage()
                d.load_default_settings()
                d.dump()
                return HttpResponseRedirect("worldmap/")
            elif (button == "B"):
                return HttpResponseRedirect("/options/load_game/")
    return render(request, "titleScreen.html", {"buttons": { "a" : { "text": "New Game" }, "b": { "text" : "Load" } } } )

def     worldMap(request):
    GD.load()
    pos = GD.getPositionPlayer()
    position = {}
    x = request.GET.get('button', '')
    if (x):
        if (x == "right" and (pos[0] + 1 < settings.DEFAULT_GAME_SIZE)):
            pos[0] += 1
        elif (x == "left" and (pos[0] > 0)):
            pos[0] -= 1
        if (x == "down" and (pos[1] + 1 < settings.DEFAULT_GAME_SIZE)):
            pos[1] += 1
        elif (x == "up" and (pos[1] > 0)):
            pos[1] -= 1
        elif (x == "select"):
            return redirect("../moviedex")
        elif (x == "start"):
            return redirect("../options")
        elif (x == "b"):
            settings.TOKEN = ''
    settings.TOKEN = ''
    if (pos[0] and settings.DEFAULT_GAME_SIZE > 0):
        position["x"] = pos[0] * ( 100 / settings.DEFAULT_GAME_SIZE )
    else:
        position["x"] = 0
    if (pos[1] and settings.DEFAULT_GAME_SIZE > 0):
        position["y"] = pos[1] * ( 100 / settings.DEFAULT_GAME_SIZE )
    else:
        position["y"] = 0
    obj = { "position" : position }
    moviemon = {}
    if (random.randrange(100) < 30):
        moviemon = GD.get_random_movie()
    if (moviemon):
        token = "tokenid123"
        settings.TOKEN = token
        obj["moviemon"] = moviemon
        battle_url = "../battle/" + moviemon["imdbID"] + "?tokenid=" + token
        obj["buttons"] = { "a" : { "link" : battle_url } }
    movieball = False
    if (not moviemon and (random.randrange(100) < 25)):
        movieball = True
    if (movieball):
        obj["movieball"] = True
        GD.addAmountMovieBall()
    screen_data = {}
    screen_data["movieballs"] = settings.BALLS
    screen_data["moviemons_left"] = len(settings.MOVIES)
    screen_data["moviemons_total"] = settings.SIZE_MOVIE
    obj["screen_data"] = screen_data
    return render( request, "worldMap.html", obj )

def     battle(request, moviemon_id):
    obj = { }
    obj["server_token"] = settings.TOKEN
    obj["request_token"] = request.GET.get('tokenid')
    if (settings.TOKEN == request.GET.get('tokenid')):
        GD.load()
        init = Data()
        data = init.get_movie_by_id(moviemon_id)
        obj["movie"] = data
        x = request.GET.get('button', '')
        if x == "a" :
            if ((settings.BALLS > 0)):
                tmp2 = data["imdbRating"] or 5.2
                tmp = int(float(tmp2))
                GD.removeAmountMovieBall()
                GD.dump()
                strengthPlayer = GD.get_strength()
                c = 50 - (tmp * 100) + (strengthPlayer * 5)
                if (c <= 1):
                    c = (1)
                elif (c >= 90):
                    c = (90)

                if (random.randrange(10) < c):
                    obj["win"] = True
                    GD.addListMovieId(data["imdbID"])
                    settings.MOVIES.remove(data["Title"])
                    GD.dump()
        screen_data = {}
        screen_data["movieballs"] =  settings.BALLS
        screen_data["moviemons_left"] = len(settings.MOVIES)
        screen_data["moviemons_total"] = settings.SIZE_MOVIE
        obj["screen_data"] = screen_data
        token = "tokenid" + str(random.randrange(9000, 100500))
        settings.TOKEN = token
        battle_url = "../battle/" + data["imdbID"] + "?tokenid=" + token + "&button=a"
        obj["buttons"] = { "a" : { "link" : battle_url }, "b" : { "link" : "../worldmap" } }
        obj["newtoken"] = token
        obj["power"] = GD.get_strength()
        return render(request, "battle.html", obj)
    else:
        return redirect("..")

def     options(request):
    settings.INDEX = 0
    listParam = {
        "buttons": {
            "a": { "text": "Save" },
            "b": { "text": "Quite" },
            "start": {"text" : "Cancel"}
        },
    }
    if request.method == "GET":
        button = request.GET.get('button')
        if button:
            if (button == "A"):
                return HttpResponseRedirect("/options/save_game/")
            elif (button == "B"):
                return HttpResponseRedirect("/")
            elif (button == "start"):
                return HttpResponseRedirect("/worldmap/")
    return render(request, "options.html", listParam)

def     saveGame(request):
    listParam = {
        "slots": [
        {"name": "slotA", "status" : "Free"},
        {"name": "slotB", "status" : "Free"},
        {"name": "slotC", "status" : "Free"},
        ],
        "buttons": {
            "a": { "text": "Save" },
            "b": { "text": "Cancel" }
        },
        "selectedMenuItemIndex" : 0
    }
    arrayPath = init_slot(listParam)
    selectedMenuItemIndex = 0
    if request.method == "GET":
        button = request.GET.get('button')
        if button:
            if (button == "A"):
                save_game_file(arrayPath)
                init_slot(listParam)
                selectedMenuItemIndex = 0
                settings.INDEX = 0
                listParam["selectedMenuItemIndex"] = selectedMenuItemIndex
                return render(request, "saveGame.html", listParam)
            elif (button == "B"):
                settings.INDEX = 0
                return HttpResponseRedirect("/options/")
            elif (button == "up"):
                selectedMenuItemIndex = ( (settings.INDEX - 1) % 3 )
            elif (button == "down"):
                selectedMenuItemIndex = ( (settings.INDEX + 1) % 3 )
    settings.INDEX = selectedMenuItemIndex
    listParam["selectedMenuItemIndex"] = selectedMenuItemIndex
    return render(request, "saveGame.html", listParam)

def     loadGame(request):
    listParam = {
        "slots": [
        {"name": "slotA", "status" : "Free"},
        {"name": "slotB", "status" : "Free"},
        {"name": "slotC", "status" : "Free"},
        ],
        "buttons": {
            "a": { "text": "Load" },
            "b": { "text": "Cancel" }
        },
        "selectedMenuItemIndex" : 0
    }
    arrayPath = init_slot(listParam)
    selectedMenuItemIndex = 0
    if request.method == "GET":
        button = request.GET.get('button')
        if button:
            if (button == "A"):
                if (settings.LOAD_FLAG == 1):
                    settings.LOAD_FLAG = 0
                    d = DataStorage()
                    dictTmp = d.load()
                    tmp = dictTmp["listMovieId"]
                    i = 0
                    for x in tmp:
                        if (settings.MOVIES == x):
                            settings.MOVIES.pop(i)
                        i += 1
                    return HttpResponseRedirect("/worldmap/")
                else:
                    r = load_progress(listParam, arrayPath)
                    if (r == True):
                        settings.LOAD_FLAG = 1
                    else:
                        settings.LOAD_FLAG = 0
                        listParam["selectedMenuItemIndex"] = 0
                        settings.INDEX = 0
                    return render(request, "loadGame.html", listParam)
            elif (button == "B"):
                settings.LOAD_FLAG = 0
                return HttpResponseRedirect("/")
            elif (button == "up"):
                selectedMenuItemIndex = ( (settings.INDEX - 1) % 3 )
            elif (button == "down"):
                selectedMenuItemIndex = ( (settings.INDEX + 1) % 3 )
    settings.INDEX = selectedMenuItemIndex
    listParam["selectedMenuItemIndex"] = selectedMenuItemIndex
    settings.LOAD_FLAG = 0
    return render(request, "loadGame.html", listParam)


def     detail(request, moviemon_id):
    movies = GD.getMoviesById()['Movies']
    data = movies[0]
    x = request.GET.get('button', '')
    if (x):
        if (x == "B"):
            return redirect("../moviedex/")
    view = { "movie" : data }
    return render(request, "detail.html", view)

def     moviedex(request):
    d = GD
    movies = GD.getMoviesById()['Movies']
    x = request.GET.get('button', '')
    selectedMenuItemIndex = 0
    if (x):
        if (x == "select"):
            return redirect("../worldmap")
        elif (len(movies)):
            if (x == "A"):
                selectedMenuItemIndex = d.getSelectedMenuItemIndex()
                return redirect("../moviedex/" + movies[selectedMenuItemIndex]['imdbID'])
            elif (x == "down"):
                selectedMenuItemIndex = ( (settings.INDEX + 1) % len(movies) )
            elif (x == "up"):
                selectedMenuItemIndex = ( (settings.INDEX - 1) % len(movies) )
    settings.INDEX = selectedMenuItemIndex
    view = { "movies" : movies, "selectedMenuItemIndex" : selectedMenuItemIndex }
    return render(request, "moviedex.html", view)

def     randomMovie(request):
    init = Data()
    data = init.get_random_movie()
    view = { "movie" : data }
    return render(request, "detail.html", view)