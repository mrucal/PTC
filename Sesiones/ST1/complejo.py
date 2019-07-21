# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:21:03 2017

@author: Mario
"""


class Complejo:
    
    def __init__(self, pr, pim):
        self.real, self.imaginario = pr, pim
        
    def __add__(self, c):
        return Complejo(self.real + c.real, self.imaginario + c.imaginario)
    
    def __sub__(self, c):
        return Complejo(self.real - c.real, self.imaginario - c.imaginario)
    
    def __mul__(self, c):
        return Complejo((self.real * c.real)-(self.imaginario * c.imaginario), (self.real * c.imaginario)+(self.imaginario * c.real))
    
    def __repr__(self):
        return '('+str(self.real)+', '+str(self.imaginario)+'i)'
    
if __name__ == '__main__':
    
    c1 = Complejo(5,2)
    c2 = Complejo(3,4)
    
    print(c1,c2,c1+c2,c1-c2,c1*c2)