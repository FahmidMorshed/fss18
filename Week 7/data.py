# -*- coding: utf-8 -*-
"""
Data class & Main File
Created on Mon Sep 10 12:03:01 2018

@author: Fahmid
"""
from config import Config
import random


class Data:
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.clss = None
        self.rows = []
        self.name = []
        self._use = {}
        self.indeps = {}
    
    def indep(self, c):
        return self.w.get(c) is not None and self.clss != c
    
    def dep(self, c):
        return not self.indep(c)
    

    """
    Calculate the dom score between two rows. It uses normalize function to first normalize
    the values. Then shouts the difference. 
    
    Param:
        List row1 - the values of row1
        List row2 - the values of row2
        
    Return: 
        Boolean 
    """
    def dom(self, row1, row2):
        n = len(self.w)
        s1 = 0
        s2 = 0
        for c, x in self.w.items():
            a = numNorm(self.nums[c], row1[c])
            b = numNorm(self.nums[c], row2[c])
            s1 = s1 - 10**(x * (a-b)/n)
            s2 = s2 - 10**(x * (b-a)/n)
        return s1/n < s2/n 

    
    """
    Append new column in the name field. Then calls the dom to calculate the dom score for
    each column.
    
    Param:
        Void
        
    Return:
        Void
    """
    def doms(self):
        n = Config().sample
        self.name.append(">dom")
        for row1 in self.rows:
            row1.append(0)
            for i in range(0,n):
                randNum = random.randint(0,len(self.rows) -1)
                row2 = self.rows[randNum]
            #for row2 in self.rows:
                if(row1==row2):
                    continue
                if(self.dom(row1, row2)):
                    row1[-1] += 1/n

"""
Calculate normalized value of x. num carries the value of hi & low

Param:
    Object Num - the values of hi and lo is inside
    Float x - the value to be normalized

Return:
    Float normalizedValue
"""
def numNorm(num, x):
    hi = num.hi
    lo = num.lo
    return (x - lo)/(hi - lo)


