# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:46:33 2017

@author: Mario
"""


import traspuesta

# SIN TERMINAR
def multiplicar(m1, m2):
    
    m2 = traspuesta.traspuesta(m2)
    
    m = []
    
    for i in m1:
        for j in m2:
            m_n = []
            print(i,j)
            for k in i:
                sum = 0
                for l in j:
                    sum += k*l
                    print(k,l)
                m_n.append(sum)
        m.append(m_n)
        
    print(m)
    return m

if __name__ == '__main__':
    
    multiplicar([[2,0],[1,3]],[[-1,-1],[5,6]])