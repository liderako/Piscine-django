import sys

def     errorExit():
    print ("Unknown capital city")
    sys.exit(-1)

def     searchDict(tmpDict, s):
    for x in tmpDict:
        res = tmpDict.get(x)
        state = x
        if (res == s):
            return (state)
    errorExit()

def     run(argv):
    if (len(argv) != 2):
        return
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
    state = searchDict(capital_cities, argv[1])
    stateTwo = searchDict(states, state)
    print (stateTwo)

if __name__ == '__main__':
    run(sys.argv)