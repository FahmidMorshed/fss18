# -*- coding: utf-8 -*-
"""
Class Sym
Created on Wed Sep  5 10:46:51 2018

@author: Fahmid
"""
from __future__ import division
from testEngine import O
from simple import Sample
from config import Config
import math

class Sym:
    def __init__(self):
        self.counts = []
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None

    def syms(self, f):
        #NOT SURE f=f or function(x) return x end
        s = Sym()
        #NOT SURE for _,x in pairs(t) do symInc(s, f(x)) end
        return s
    
    def symInc(self,x):
        if x is None:
            return x
        self._ent = None
        self.n += 1
        old = self.counts[x]
        new = old and old + 1 or 1
        self.counts[x] = new
        if new > self.most:
            self.most, self.mode = new, x
        return x
    
    def symDec(self, x):
        self._ent= None
        self.n -= 1
        self.counts[x] -= 1
        return x
    
    def symEnt(self):
        if not self._ent:
            self._ent = 0
        for x, n in zip(self.counts[:-1], self.counts[1:]):
            p = n / self.n
            self._ent = self._ent - p * math.log(p,2)
            
        return self._ent
    
    
    
@O.k
def baseSym():
    s=syms{ 'y','y','y','y','y','y','y','y','y',
	        'n','n','n','n','n'}
    assert (s.symEnt() == 0.9403)
    print (s.symEnt())
