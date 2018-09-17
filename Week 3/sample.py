# -*- coding: utf-8 -*-
"""
Sample Class
Created on Sat Sep 1, 2018
@author: Fahmid Morshed
"""

from __future__ import division
import random
from math import floor
from config import Config
class Sample:
    def __init__(self, myMax=Config().hi):
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


