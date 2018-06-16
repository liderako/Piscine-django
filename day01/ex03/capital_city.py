import sys
def     run(argv):
    if (len(argv) != 2):
        return
    states = {"Oregon" : "OR", "Alabama" : "AL", "New Jersey": "NJ", "Colorado" : "CO"}
    capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}
    res = states.get(argv[1])
    if res != None:
        print (capital_cities.get(res))
    else:
        print ("Unknown state")

if __name__ == '__main__':
    run(sys.argv)