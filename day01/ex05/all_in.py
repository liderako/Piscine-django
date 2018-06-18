import sys

def     deleteSpace(argv):
    result = argv[1].split(',')
    i = 0
    for x in result:
        result[i] = x.strip()
        i += 1
    i = 0
    for x in result:
        if (x == ""):
            result.pop(i)
        i += 1
    return (result)

def     searchDict(tmpDict, s):
    for x in tmpDict:
        res = tmpDict.get(x)
        state = x
        if (res == s):
            return (state)
    return (-1)

def     printS(s, capital):
    print (s, "is the capital of", capital)

def run(argv):
    if (len(argv) != 2):
        return 0
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"}
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"}
    result = deleteSpace(argv)
    if ((len(result) == 0) or (len(result) == 1 and result[0] == "")):
        return
    i = 0
    for x in result:
        if (x == ''):
            continue 
        xOld = x
        tmpS = x.capitalize()
        tmp = tmpS.split(" ")
        if (len(tmp) == 2):
            tmp[1] = tmp[1].capitalize()
            x = tmp[0] + " " + tmp[1]
        else:
            x = tmpS
        resState = searchDict(capital_cities, x)
        resCapital = states.get(x)
        if (resState == -1 and resCapital == None):
            print(xOld, "is neither a capital city nor a state")
        elif (resState != -1):
            printS(x, searchDict(states, resState))
        else:
            printS(capital_cities.get(resCapital), x)

if __name__ == '__main__':
    run(sys.argv)