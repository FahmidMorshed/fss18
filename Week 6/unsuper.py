# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:35:10 2018

@author: Fahmid
"""
from config import Config
from num import Num
from operator import itemgetter

def unsuper(data):
    rows = data.rows
    enough = len(rows)**Config().unsuperEnough
    most = 0
    
    def band(c, lo, hi):
        """
        band takes the low and hi value along with the index and return the string to be printed
        
        Param:
            int c for index of rows
            int lo for the lowest cut
            int hi for the highest cut
        
        Return:
            String
        """
        if(lo==0):
            return ".." + str(rows[hi][c])
        elif(hi == most):
            return str(rows[lo][c]) + ".."
        else:
            return str(rows[lo][c]) + ".." + str(rows[hi][c])
        
    def argmin(c, lo, hi):
        """
        finds the cut index for the min sd returns that. If cut is not found, returns None
        
        Param:
            int c for index of rows
            int lo for the lowest cut
            int hi for the highest cut
        
        Return:
            int cut index or None
        """
        cut = None
        if(hi - lo > 2 * enough):
            l = Num()
            r = Num()
            
            for i in range(lo,hi+1):
                r.numInc(rows[i][c])
            
            best = r.sd
            
            for i in range(lo,hi+1):
                x = rows[i][c]
                l.numInc(x)
                r.numDec(x)
                
                if (l.n >= enough and r.n >= enough):
                    temp = Num.numXpect(l, r)
                    if(isinstance(temp, complex)):
                        temp = temp.real
                    if(temp < best):
                        cut = i
                        best = temp
        return cut
    
    def cuts(c, lo, hi, pre):
        """
        calls the cut function recursively and gets the text to print
        
        Param:
            int c for index of rows
            int lo for the lowest cut
            int hi for the highest cut
            String pre for the text to print
        Return:
            Void
        """
        txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
        cut = argmin(c, lo, hi)
        
        if cut is not None:
            print(txt)
            cuts(c, lo, cut, pre + "|.. ")
            cuts(c, cut+1, hi, pre + "|.. ")
        else:
            b = band(c, lo, hi)
            print(txt + " (" + b + ")")
            for r in range(lo, hi+1):
                rows[r][c] = b
            
    
    def stop(c, t):
        """
        ignores the undefined data and also calculates the most variable
       Param:
           int c for the index
           list c is the rows
       Return:
           int most
        
        """
        for i in range(len(t)-1, -1, -1):
            if(t[i][c] != Config().garbageValue):
                return i
        return 0
    
   
    for i,_ in data.indeps.items():
        
        
        if(data.nums.get(i, 0) == 0):
            continue
        
        for row in rows:
            if isinstance(row[i], str):
                row[i] = Config().garbageValue
        
        rows.sort(key=itemgetter(i))
        most = stop(i, rows)
        print("\n-- " + str(data.name[i]) + ": "+ str(most + 1) + "---------" )
        cuts(i, 0, most, "|.. ")
    
    
    