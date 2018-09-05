# -*- coding: utf-8 -*-
"""
Sample Class
Created on Sat Sep 1, 2018
@author: Fahmid Morshed
"""

from __future__ import division
from testEngine import O
import random
from math import floor

class Sample:
    def __init__(self, myMax):
        self.max = myMax
        self.n = 0
        self.sorted = False
        self.some = []
    
    def sampleInc(self, x):
        self.n += 1
        now = len(self.some)
        if (now < self.max):
            self.sorted = False
            self.some.append(x)
        elif (random.random() < now /self.n):
            self.sorted = False
            self.some[floor(0.5 + (random.random() * now))] = x
        return x
    
    def sampleSorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some
    
    def nth(self, n):
        s = self.sampleSorted()
        temp = floor(0.5 + (len(s)*n))
        temp = max(0, temp)
        return s[ min(len(s), temp) ]


"""Test Sample"""
@O.k
def sampleTest():
    random.seed(1)
    s = []
    for i in range(5,6):
        s.append(Sample(2**i))
    for i in range (1,1001):
        y = random.random()
        for _,t in zip(s[:-1], s[1:]):
            t.sampleInc(y)
    
    for _,t in zip(s[:-1], s[1:]):
        print (t.max, t.nth(t, 0.5))
        assert ((0.5 > t.nth(t,0.5)) and (t.nth(t,0.5) > 0.25)) #confused +- .2 of .5
