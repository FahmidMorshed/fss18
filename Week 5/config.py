# -*- coding: utf-8 -*-
"""
Config file
Created on Tue Sep  4 13:37:00 2018

@author: Fahmid
"""

class Config:
    def __init__(self):
        self.lo = 10**32
        self.hi = -10**32
        self.maxRowsToPrint = 30
        self.unsuperEnough = 0.5 #MAGIC
        self.unsuperMargin = 1.05 #MAGIC
        self.sample = 100 #MAGIC
        self.garbageValue = 999999 #Used to replace ?