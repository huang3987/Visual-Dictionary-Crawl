import os
from KB_Mouse import *
import KB_Mouse
import time
import clipboard

path = os.getcwd()
filenames = os.listdir(path)
#print filenames 350,700
temp = []
for filename in filenames:
    #print filename[-3:]
    if filename[-3:] == "dec":
        temp.append(filename)
filenames = temp[:]
temp = []
for filename in filenames:
    with open(filename) as deck:
        deckname = deck.readline()
        #print deckname
        clipboard.copy(deckname)
        Mouse.click(350,700,1,1)
        time.sleep(0.5)
        Paste()
        KB.tap_key(KB.enter_key)

