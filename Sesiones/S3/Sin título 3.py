# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:42:06 2017

@author: Mario
"""

def orden_alfabetico(cad):

    cad = cad.lower()

    for i in range(len(cad)-1):
        if ord(cad[i]) >= 97 and ord(cad[i]) <= 122 and ord(cad[i+1]) >= 97 and ord(cad[i+1]) <= 122:
            if cad[i] >= cad[i+1]:
                return False

    return True