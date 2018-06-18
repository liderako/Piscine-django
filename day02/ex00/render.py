import sys, os, re
from settings import *

def read(fileName):
    match = re.search(r'.template', fileName)
    try:
        if (match == None):
            sys.exit(-1)
    except:
        errorExit("Error including a bad file extension. Please use file <.template>")
    try:
        f = open(fileName, 'r')
        return (f.read())
    except:
        errorExit("File read error. I'm sorry friend ^_^ Maybe file that does not exist.")

def errorExit(message):
    print (message)
    sys.exit(-1)

def writeFile(fileName, message):
    fileObject = open(fileName, "w")
    fileObject.write(message)
    fileObject.close()

def run(argc, argv):
    if (argc != 2):
        errorExit("Please =) Usage: python render.py myCV.template ")
    else:
        buffer = read(sys.argv[1])
        buffer = buffer.replace("{age}", age)
        buffer = buffer.replace("{name}", name)
        buffer = buffer.replace("{lastName}", lastName)
        buffer = buffer.replace("{job}", job)
        writeFile(sys.argv[1].replace(".template", ".html"), buffer)

if __name__ == '__main__':
    run(len(sys.argv), sys.argv)