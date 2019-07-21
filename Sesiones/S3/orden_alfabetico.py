# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:49:12 2017

@author: Mario
"""


def orden_alfabetico(cad):

    cad = cad.lower()
    cad_aux = ""

    # Eliminar caracteres distintos de letras
    for i in cad:
        if ord(i) >= 97 and ord(i) <= 122:
            cad_aux = cad_aux + i

    for i in range(len(cad_aux)-1):
        if cad_aux[i] >= cad_aux[i+1]:
            return False

    return True


if __name__ == '__main__':

    # 1 cadena vacía: Correcto
    if (orden_alfabetico("")):
        print("1. Correcto")
    else:
        print("1. Incorrecto")

    # 2 un carácter: Correcto
    if (orden_alfabetico("a")):
        print("2. Correcto")
    else:
        print("2. Incorrecto")

    # 3 dos carácteres desordenados: Incorrecto
    if (orden_alfabetico("aA")):
        print("3. Correcto")
    else:
        print("3. Incorrecto")

    # 4 cadena ordenada (algunas en mayuscula): Correcto
    if (orden_alfabetico("abCtu")):
        print("4. Correcto")
    else:
        print("4. Incorrecto")

    # 5 cadena ordenada (algunas en mayuscula) y con caracters especiales:
    #   Correcto
    if (orden_alfabetico("abC, tu")):
        print("5. Correcto")
    else:
        print("5. Incorrecto")

    # 5b igual que el anterior, con mas de dos caracteres especiales seguidos:
    #    Correcto
    if (orden_alfabetico("abC,   d, tu")):
        print("5b. Correcto")
    else:
        print("5b. Incorrecto")

    # 6 cadena desordenada: Incorrecto
    if (orden_alfabetico("abCea,tu")):
        print("6. Correcto")
    else:
        print("6. Incorrecto")
