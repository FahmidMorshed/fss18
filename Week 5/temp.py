# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:31:39 2018

@author: Fahmid
"""

          
class Data:
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.clss = None
        self.rows = {}
        self.name = {}
        self._use = {}
    
    def indep(self, c):
        return not self.w[c] and self.clss != c
    
    def dep(self, c):
        return not self.indep(c)
    
    def header(self, cells):
        for c0,x in enumerate(cells):
            if not re.match("%?", x):
                c = len(self._use) + 1
                self._use[c] = c0
                self.name[c] = x
                if re.match("[<>%$]"):
                    self.nums[c] = Num()
                else:
                    self.syms[c] = Sym()
                
                if re.match("<"):
                    self.w[c] = -1
                elif re.match(">"):
                    self.w[c] = 1
                elif re.match("!"):
                    self.clss = c
                else:
                    self.indep(c)
        
    def rows(self, cells):
        r = len(self.rows) + 1
        
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            if (x != "?"):
                if(self.nums.get(c,0) != 0):
                    x = float(x)
                    self.nums.get(c).numInc(x)
                else:
                    self.syms.get(c).symInc(x)
            self.rows.
    
    t.rows[r] = {}
  for c,c0 in pairs(t._use) do
    x = cells[c0]
    if x ~= "?" then
      if t.nums[c] then 
	x = tonumber(x)
        numInc(t.nums[c], x)
      else
	symInc(t.syms[c], x)
    end end
    t.rows[r][c] = x  end
  return t
