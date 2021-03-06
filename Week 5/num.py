# -*- coding: utf-8 -*-
"""
Num Class
Created on Tue Sep  4 13:32:35 2018

@author: Fahmid
"""

from __future__ import division
from testEngine import O
from sample import Sample
from config import Config
class Num:
    def same(x): 
        return x
    
    def __init__(self, initList=[], f=same):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = Config().lo
        self.hi = Config().hi
        self.some = Sample()
        self.w = 1
        [self.numInc(x) for x in initList]
        
    
    def numInc(self, x):
        if x is None: 
            return x
        self.n += 1
        self.some.sampleInc(x)
        d = x - self.mu
        self.mu +=  (d/self.n)
        self.m2 += (d*(x-self.mu))
        
        if(x > self.hi):
            self.hi = x
        if(x < self.lo):
            self.lo = x
        if(self.n >= 2):
            self.sd = ((self.m2/(self.n - 1 + (10**-32)))**(.5))
        return x
    
    def numDec(self, x):
        if x is None:
            return x
        if(self.n == 1): 
            return x
        self.n -= 1
        d = x - self.mu
        self.mu -= (d/self.n)
        self.m2 -= (d*(x-self.mu))
        
        if(self.n >= 2):
            self.sd = ((self.m2/(self.n - 1 + (10**-32)))**(.5))
        return x
        
    def numNorm(self, x):
        return (x-self.lo) / (self.hi-self.lo + (10**-32))

    def numXpect(i, j):
        n = i.n + j.n + .0001
        return i.n/n * i.sd + j.n/n * j.sd
    
    

@O.k
def numOkay():
    n = Num([4,10,15,38,54,57,62,83,100,100,174,190,215,225,
       233,250,260,270,299,300,306,333,350,375,443,475,
       525,583,780,1000])
    print (n.mu)
    print (round(n.sd,3))
    assert n.mu == 270.3
    assert round(n.sd,3) == 231.946
    