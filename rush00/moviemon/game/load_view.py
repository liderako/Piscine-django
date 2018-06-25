from django.conf import settings
from .object.DataStorage import DataStorage
import glob
import os

def     if_file(name):
    try:
        file = open(name)
        return (True)
    except:
        return (False)

def     setSlot(slots, i, string):
    tmp_slot = slots[i]
    tmp_slot["status"] = string
    slots[i] = tmp_slot

def     save_elem(listFind, listRes, str):
    for x in listFind:
        if (x.find(str)) != -1:
            listRes.append(x)
            break

def     getFileName():
    listName = glob.glob(settings.SAVED_PATH+"*.mmg")
    i = 0
    while i < len(listName):
        listName[i] = listName[i].replace(settings.SAVED_PATH, "")
        i += 1
    listRes = list()
    save_elem(listName, listRes, "slota")
    save_elem(listName, listRes, "slotb")
    save_elem(listName, listRes, "slotc")
    i = 0
    while i < len(listRes):
        listRes[i] = settings.SAVED_DIR + listRes[i]
        print (listRes[i])
        i += 1
    return (listRes)

def     ft_zero(slots, array):
    i = 0
    res = [[-1, ""], [-1, ""], [-1, ""]]
    for x in array:
        
        if (res[0][0] == -1):
            if (x[0].find("slota")) != -1:
                res[0] = [i, x[0]]
        
        if (res[1][0] == -1):
            if (x[0].find("slotb")) != -1:
                res[1] = [i, x[0]]
        
        if (res[2][0] == -1):
            if (x[0].find("slotc")) != -1:
                res[2] = [i, x[0]]
        i += 1
    if (res[0][0] == -1):
        setSlot(slots, 0, "Free")
    if (res[1][0] == -1):
        setSlot(slots, 1, "Free")
    if (res[2][0] == -1):
        setSlot(slots, 2, "Free")
    return (res)

def     ft_progress(slots, res, d):
    stringM = " Moviemons"
    if (res[0][0] != -1):
        aDict = d.load(res[0][1])
        status = str(len(aDict.get("listMovieId"))) + "/" + str(settings.SIZE_MOVIE) + stringM
        setSlot(slots, 0, status)

    if (res[1][0] != -1):
        aDict = d.load(res[1][1])
        status = str(len(aDict.get("listMovieId"))) + "/" + str(settings.SIZE_MOVIE) + stringM
        setSlot(slots, 1, status)

    if (res[2][0] != -1):
        aDict = d.load(res[2][1])
        status = str(len(aDict.get("listMovieId"))) + "/" + str(settings.SIZE_MOVIE) + stringM
        setSlot(slots, 2, status)

# def     get_amount_movie()

def     init_slot(listParam):
    listName = getFileName()
    array = list()
    
    for x in listName:
        array.append([x, if_file(x)])
    slots = listParam.get("slots")

    d = DataStorage()
    d.load_default_settings()
    res = ft_zero(slots, array)
    ft_progress(slots, res, d)
    return (res)

def     changeData(listParam, arrayPath):
    d = DataStorage()
    if (settings.INDEX == 0):
        tmp_dict = d.load(arrayPath[0][1])
    elif (settings.INDEX == 1):
        tmp_dict = d.load(arrayPath[1][1])
    elif (settings.INDEX == 2):
        tmp_dict = d.load(arrayPath[2][1])
    d.setPositionPlayer(tmp_dict["positionPlayer"])
    d.setAmountMovieBall(tmp_dict["amountMovieBall"])
    d.setListMovieId(tmp_dict["listMovieId"])
    d.setDataMovieIMDV(tmp_dict["dataMovieIMDB"])
    d.setSelectedMenuItemIndex(tmp_dict["selectedMenuItemIndex"])
    d.dump()
    return (True)

def     changeText(buttons, res, slotI):
    if (res == "Free"):
        return (False)
    buttons['a'] = {"text" : "Start Game"}
    return (True)


def     load_progress(listParam, arrayPath):
    r = False
    slots = listParam.get("slots")
    buttons = listParam.get("buttons")
    if (settings.INDEX == 0):
        res = slots[0].get("status")
        r = changeText(buttons, res, 0)
    elif (settings.INDEX == 1):
        res = slots[1].get("status")
        r = changeText(buttons, res, 1)
    elif (settings.INDEX == 2):
        res = slots[2].get("status")
        r = changeText(buttons, res, 2)
    if (r == True):
        changeData(listParam, arrayPath)
        return (True)
    return (False)

def     save_game_file(arrayPath):
    d = DataStorage()
    try:
        tmp_dict = d.load()
    except FileNotFoundError:
        d.load_default_settings()
        d.dump()
        tmp_dict = d.load()
    if (settings.INDEX == 0):
        name = "slota"
        if (arrayPath[0][0] != -1):
            os.remove(arrayPath[0][1])
    elif (settings.INDEX == 1):
        name = "slotb"
        if (arrayPath[1][0] != -1):
            os.remove(arrayPath[1][1])
    elif (settings.INDEX == 2):
        name = "slotc"
        if (arrayPath[2][0] != -1):
            os.remove(arrayPath[2][1])
    name = settings.SAVED_DIR + name + "_" + str(len(tmp_dict.get("listMovieId"))) + "_" + str(settings.SIZE_MOVIE) + ".mmg"
    d.setPositionPlayer(tmp_dict["positionPlayer"])
    d.setAmountMovieBall(tmp_dict["amountMovieBall"])
    d.setListMovieId(tmp_dict["listMovieId"])
    d.setDataMovieIMDV(tmp_dict["dataMovieIMDB"])
    d.setSelectedMenuItemIndex(tmp_dict["selectedMenuItemIndex"])
    d.dump(name)