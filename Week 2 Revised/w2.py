# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:02:22 2018

@author: Fahmid
"""

import sys, zipfile, codecs, re
from testEngine import O

DATA1 = """
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""


DATA2 = """
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes
    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,
       
                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""
    
    
def lines(src=None, f=None):
    if src is None:
        #no string is given, read from standard input
        for line in sys.stdin:
            yield line
    elif src[-4:] == ".zip" :
        #src ends with .zip, so unzip it first and then read
        #for zip, also give the filename inside the zip in arg f
        with zipfile.ZipFile(src, 'r') as z:
            with z.open(f, 'r') as f:
                for line in f:
                    yield codecs.decode(line,'unicode_escape')
    elif src[-4:] in [".csv", ".dat"]:
        with open(src) as fs:
            for line in fs:
                yield line
    else:
        for line in src.splitlines():
            yield line

def rows(src):
    cache = []
    #the cache works nicely for joining with the next line
    for line in src:
        line = re.sub(r'([ \n\r\t]|#.*)', "", line)
        cache += [line]
        if len(line)> 0:
            if line[-1] != ",":
                line = ''.join(cache)
                cache = []
                yield line
                
def cols(src, uses=None):
    #the uses is a nice trick and the trinarry operator is lovely
    for row in src:
        cells = row.split(",")
        uses = uses or [False if "?" in s[0] else True for s in cells]
        out = [cells[pos] for pos, use in enumerate(uses) if use]
        yield out

def prep(src, nums=None):
    for xs in src:
        if nums:
            xs= [(float(x) if num else x) for x,num in zip(xs,nums)]
        else:
            nums = ["$" in x[0] for x in xs]
        return xs

for line in rows(lines(DATA1)):
    print(line) 




def ok0(s=None):
    for row in prep(cols(rows(lines(s)))):
        print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)

@O.k
def ok3(): 
    """If this hangs, just hit control-d and next time you run it, use 
    'cat file.csv | python3 read.py'
    """
    ok0()

if __name__== "__main__":
    O.report()                       
                