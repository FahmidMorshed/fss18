# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:31:42 2018

@author: Fahmid
"""

import sys, zipfile, codecs, re, data
from testEngine import O
from num import Num
from sym import Sym


"""
Dom function calculates the domination score of two rows for multi objective
optimization.

Parameters
----------
t
    t contains a Data object
    type: Data
    first parameter
row1
    type: int
    second parameter
    
row2
    type: int
    third parameter
"""
def dom(t, row1, row2):
    n = len(t.w)
    s1 = 0
    s2 = 0
    for c, w in enumerate(t.w):
        a = numNorm(t.nums[c], row1[c])
        b = numNorm(t.nums[c], row2[c])
        s1 = s1 - 10^(w * (a-b)/n)
        s2 = s2 - 10^(w * (b-a)/n)
    return s1/n < s2/n 



def doms(t):
    c = len(t.name) + 1
    print(cat(t.name,",") + ",>dom")
    for row1 in t.rows:
        row1.append(0)
        for row2 in t.rows:
            if(row1==row2):
                continue
            s = dom(t, row1, row2) and 1/n or 0
            row1[-1] = row1[-1] + s
            
            
            
function doms(t,  n,c,row1,row2,s)
  n= Lean.dom.samples
  c= #t.name + 1
  print(cat(t.name,",") .. ",>dom")
  for r1=1,#t.rows do
    row1 = t.rows[r1]
    row1[c] = 0
    for s=1,n do
     row2 = another(r1,t.rows) 
     s = dom(t,row1,row2) and 1/n or 0
     row1[c] = row1[c] + s end end
  dump(t.rows)
end
