# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:07:01 2017

@author: Mario
"""


def vector_disperso(v):
        
    l = []
    
    for i in range(len(v)):
        if v[i] != 0:
            l.append((i, v[i]))
            
    return (l, len(v))


def vector_disperso_inverso(vd):
    
    v = [0] * vd[1]
    
    for i in vd[0]:
        v[i[0]] = i[1]
        
    return v


def vector_disperso_matriz(v):
    
    vdm = []

    for i in v:
        vdm.append(vector_disperso(i))
    
    return tuple(vdm)

def vector_disperso_inverso_matriz(vd):
    
    vm = []
    
    for i in vd:
        vm.append(vector_disperso_inverso(i))
        
    return vm

if __name__ == '__main__':
    print("VD:",vector_disperso([1,0,0,3,4,7,0,0,2]))
    print("VDI:",vector_disperso_inverso(([(0, 1), (3, 3), (4, 4), (5, 7), (8, 2)], 9)))
    
    
    print("VDM:",vector_disperso_matriz([[1,0,0,3],[4,7,0,0,2]]))
    print("VDMI:",vector_disperso_inverso_matriz((([(0, 1), (3, 3)], 4), ([(0, 4), (1, 7), (4, 2)], 5))))