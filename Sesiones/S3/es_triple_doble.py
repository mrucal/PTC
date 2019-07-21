# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:26:07 2017

@author: Mario
"""

def es_triple_doble(cad):
    
    for i in range(len(cad)-1):
        if cad[i] == cad[i+1] and i < len(cad)-5:
            if cad[i+2] == cad[i+3]:
                if cad[i+4] == cad[i+5]:
                    return True
    return False


if __name__ == '__main__':

    # 1 Incorrecto
    if es_triple_doble(""):
        print("1. Correcto")
    else:
        print("1. Incorrecto")

    # 2 Correcto
    if es_triple_doble("aabbcc"):
        print("2. Correcto")
    else:
        print("2. Incorrecto")

    # 3 Correcto
    if es_triple_doble("eaabbcce"):
        print("3. Correcto")
    else:
        print("3. Incorrecto")

    # 4 Incorrecto
    if es_triple_doble("eaabebcce"):
        print("4. Correcto")
    else:
        print("4. Incorrecto")

    # 5 Correcto
    if es_triple_doble("rfseaabbcc"):
        print("5. Correcto")
    else:
        print("5. Incorrecto")
