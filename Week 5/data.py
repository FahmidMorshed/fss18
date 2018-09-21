# -*- coding: utf-8 -*-
"""
Data class & Main File
Created on Mon Sep 10 12:03:01 2018

@author: Fahmid
"""
import sys, zipfile, codecs, re
from testEngine import O
from num import Num
from sym import Sym

class Data:
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.clss = None
        self.rows = []
        self.name = {}
        self._use = {}
        self.indeps = {}
    
    def indep(self, c):
        return self.w.get(c) is not None and self.clss != c
    
    def dep(self, c):
        return not self.indep(c)
    

    
    def dom(self, row1, row2):
        n = len(self.w)
        s1 = 0
        s2 = 0
        for c, x in self.w.items():
            #TODO: normalize
            a = numNorm(self.nums[c], row1[c].get(c))
            b = numNorm(self.nums[c], row2[c].get(c))
            s1 = s1 - 10**(x * (a-b)/n)
            s2 = s2 - 10**(x * (b-a)/n)
        return s1/n < s2/n 

    

    def doms(self):
        print(str(self.name) + ",>dom")
        for row1 in self.rows:
            row1.append(0)
            for row2 in self.rows:
                if(row1==row2):
                    continue
                if(self.dom(row1, row2)):
                    row1[-1] += 1/len(self.rows) 
 
def numNorm(num, x):
    hi = num.hi
    lo = num.lo
    return (x - lo)/(hi - lo)

def addRow(data, cells):
    tempRows = []
    for i, use in data._use.items():
        if(use==True):
            x = cells[i]
            if("?" not in x):
                if(data.nums.get(i, 0) != 0):
                    x = float(x)
                    data.nums.get(i).numInc(x)
                else:
                    data.syms.get(i).symInc(x)
            tempRows.append({i: x})
    data.rows.append(tempRows)

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

def header(data, cells):
    for i,x in enumerate(cells):
        if "%?" not in x:
            data._use[i] = True
            data.name[i] = x
            if re.search(r"[<>$]", x):
                data.nums[i] = Num()
            else:
                data.syms[i] = Sym()
            
            if re.search(r"<", x):
                data.w[i] = -1
            elif re.search(r">", x):
                data.w[i] = 1
            elif re.search(r"!", x):
                data.clss = i
            else:
                data.indeps[i] = True
        else:
            data._use[i] = False

                           

def printResult(csvFilename):
    first = True
    data = Data()
    for x in rows(lines(csvFilename)):
        if(first):
            first = False
            header(data, x.split(","))
        else:
            addRow(data, x.split(","))
    
    print ("#\tName\t\t n \t       mode \t       freq")        
    for i, x in data.syms.items():
        print ("%d   %15s \t %d \t %10s \t %10.2f" % (i, data.name[i], x.n, x.mode, x.most))
        #print(str(i) + "\t" + data.name[i][:7] + ".." + "\t" + str(x.n))
    
    
    print ("\n#\tName\t\t n \t\t mu \t\t sd")        
    for i, x in data.nums.items():
        print ("%d   %15s \t %d \t %10.2f \t %10.2f" % (i, data.name[i], x.n, x.mu, x.sd))
    
    data.doms()
    
    data.rows.sort(key=sortByDom)
    
    for row in data.rows:
        row[-1] = round(row[-1], 2)
        print(row)


def sortByDom(row):
    return row[-1]

@O.k
def test():
    print ('=========Testing on "auto.csv"=============')
    printResult("auto.csv")
    
    #print('\n\n')
    #print ('=========Testing on "weather.csv"==========')
    #printResult("weather.csv")
    
    #print('\n\n')
    #print ('=======Testing on "weatherLong.csv"========')
    #printResult("weatherLong.csv")
    assert 1==1