def my_var():
    tmpInt = 42
    tmpStr = "42"
    tmpStrTwo = "quarante-deux"
    tmpFloat = 42.0
    tmpBool = True
    tmpList = [42]
    tmpDict = {42: 42}
    tmpTuple = (42,)
    tmpSet = set()
    print (tmpInt, "est de type", type(tmpInt))
    print (tmpStr, "est de type", type(tmpStr))
    print (tmpStrTwo, "est de type", type(tmpStrTwo))
    print (tmpFloat, "est de type", type(tmpFloat))
    print (tmpBool, "est de type", type(tmpBool))
    print (tmpList, "est de type", type(tmpList))
    print (tmpDict, "est de type", type(tmpDict))
    print (tmpTuple, "est de type", type(tmpTuple))
    print (tmpSet, "est de type", type(tmpSet))

if __name__ == '__main__':
    my_var()
