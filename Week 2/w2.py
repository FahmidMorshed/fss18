# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 19:07:01 2018

@author: Fahmid Morshed
"""

import re, traceback
from collections import defaultdict

class O():
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


"""These are the sample data"""
DATA1 ="""
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

DATA2 ="""
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

"""My Code to read table"""


def lines(s):
    "Return contents, one line at a time."
    if(s is None):
        return None
    else:
        return [x for x in s.split("\n") if x!= ""] 
        
    

def rows(src):
    """Kill bad characters. If line ends in ',' 
    then join to next. Skip blank lines."""
    filteredString = ""
    for line in src:
        line = re.sub(r"\s+", "", line)
        if "#" in line:
            line = line.split("#")[0]
        if not line.endswith(",") :
            filteredString += line + "\n"
        else:
            filteredString += line
    return filteredString.split("\n")

def cols(src):
    """ If a column name on row1 contains '?', 
    then skip over that column."""
    allLines = []
    for line in src:
        if(line==""): continue
        words = line.split(",")
        allLines.append(words)
    
    ignoreFlag = defaultdict(int)

    count = 0
    for word in allLines[0]:
        if "?" in word:
            ignoreFlag[count] = 1
        else:
            ignoreFlag[count] = 0
        count += 1
        
        
    firstRow = allLines[0]
    attributes = []
    filteredLines = []
    
    for word in firstRow:
        if not "?" in word:
            attributes.append(word)
            
    filteredLines.append(attributes)
    allLines = allLines[1:]
    filteredWords = []
    
    for line in allLines:
        for i in range(len(line)):
            if(ignoreFlag.get(i)==0):
                filteredWords.append(line[i])
        filteredLines.append(filteredWords)
        filteredWords = []
    return filteredLines

def prep(src):
    """ If a column name on row1 contains '$', 
    coerce strings in that column to a float."""
    finalList = []
  
  
    floatFlag = defaultdict(int)

    count = 0
    
    
    for word in src[0]:
        if "$" in word:
            floatFlag[count] = 1
        else:
            floatFlag[count] = 0
        count += 1
  
    finalList = [src[0]]
    src = src[1:]
    for line in src:
        tempList = []
        for i in range(len(line)):
            word = line[i]
            if(floatFlag[i]==1):
                tempList.append(float(word))
            else:
                tempList.append(word)
        finalList.append(tempList)
    
    
    return finalList









"""This is the unit test"""
def ok0(s):
  for row in prep(cols(rows(lines(s)))):
    print(row)


@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)
