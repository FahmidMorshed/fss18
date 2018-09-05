# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 13:17:07 2018

@author: Fahid
"""

import re, traceback
from collections import defaultdict


"""Test Engine"""
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
"""End of Test Engine"""


"""Data"""
data = [4,10,15,38,54,57,62,83,100,100,174,190,
        215,225,233,250,260,270,299,300,306,
        333,350,375,443,475,525,583,780,1000]

"""Class"""
class Config():
    def __init__(self):
        self.low = 10**32
        self.hi = 10**32
    

class Num():
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.sd = 0
        self.lo = Config.low
        self.hi = Config.hi
        self.some = sample()
        self.w = 1
    
    
    def nums(self, f):
        n = Num()
        for _,x in zip(self[:-1], self[1:]):
            numInc(n, f(x))
        return n


def numTest(data):
    print ("Num Test")
    print (data.mu)
    print (data.sd)
    assert (data.mu == 123)
    assert (data.sd == 10)
    
