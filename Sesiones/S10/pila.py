# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:04:27 2017

@author: Mario
"""

class pila:
    
    p = []
    
    def __init__(self):
        self.p = []
        
    def add_item(self,item1,item2=None):
        self.p += [item1]
        if item2 != None:
            self.p += [item2]
        
    def pop_item(self):
        if len(self.p) > 0:
            pop = self.p[-1]
            del self.p[-1]
            return pop
        else:
            return False
        
    def count_items(self):
        return len(self.p)
        
if __name__ == "__main__" :  
    s = pila()
    s.add_item(5)
    print(s.p)
    s.add_item(4,10)
    print(s.count_items())
    print(s.p)
    s.pop_item()
    print(s.p)
    print(s.count_items())
