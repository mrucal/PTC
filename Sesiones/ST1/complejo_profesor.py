# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:21:03 2017

@author: Mario
"""


class Complejo:
    
    def __init__(self, pr=1.0, pim=0.0):
        self.real, self.imaginario = float(pr), float(pim)
        
    def __add__(self, c):
        if type(c) == Complejo:
            return Complejo(self.real + c.real, self.imaginario + c.imaginario)
        else:
            if type(c) == int or type(c) == float:
                return Complejo(self.real + c, self.imaginario)
            else:
                print('no implementado')
                
    def __radd__(self, c):
        if type(c) == int or type(c) == float:
            return Complejo(c+self.real, self.imaginario)
        else:
            print('no implementado')
    
    def __sub__(self, c):
        return Complejo(self.real - c.real, self.imaginario - c.imaginario)
    
    def __mul__(self, c):
        return Complejo((self.real * c.real)-(self.imaginario * c.imaginario), (self.real * c.imaginario)+(self.imaginario * c.real))
    
    def __repr__(self):
        return '('+str(self.real)+', '+str(self.imaginario)+'i)'
    
if __name__ == '__main__':
    
    c1 = Complejo(5,2)
    c2 = Complejo(3,4)
    
    print(c1,c2,c1+c2,c1-c2,c1*c2,3+c1,c1+3)