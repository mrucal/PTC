# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:17:08 2017

@author: Mario
"""


def anagrama(cad1, cad2):

    # Ordenar las letras de cada cadena
    cad1 = list(cad1)
    cad1.sort()
    cad1 = "".join(cad1)

    cad2 = list(cad2)
    cad2.sort()
    cad2 = "".join(cad2)

    return cad1 == cad2


if __name__ == '__main__':

    # 1 Correcto
    if anagrama("", ""):
        print("1. Correcto")
    else:
        print("1. Incorrecto")

    # 2 Correcto
    if anagrama("a", "a"):
        print("2. Correcto")
    else:
        print("2. Incorrecto")

    # 3 Correcto
    if anagrama("marta", "trama"):
        print("3. Correcto")
    else:
        print("3. Incorrecto")

    # 3b Incorrecto
    if anagrama("martaa", "trama"):
        print("3b. Correcto")
    else:
        print("3b. Incorrecto")

    # 3c Correcto
    if anagrama("martaa", "traama"):
        print("3c. Correcto")
    else:
        print("3c. Incorrecto")

    # 4 Incorrecto
    if anagrama("aaeee", "eeaaa"):
        print("4. Correcto")
    else:
        print("4. Incorrecto")

    # 4b Correcto
    if anagrama("aaaeee", "eeeaaa"):
        print("4b. Correcto")
    else:
        print("4b. Incorrecto")

    # 4c Correcto
    if anagrama("aaaee", "eeaaa"):
        print("4c. Correcto")
    else:
        print("4c. Incorrecto")
