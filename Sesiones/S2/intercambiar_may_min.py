# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:26:56 2017

@author: Mario
"""


def intercambiar_mayusculas_minusculas(cad):
    """Intercambia letras mayusculas y minusculas en una cadena"""

    nueva_cad = ""

    for i in cad:
        if ord(i) < 64 or ord(i) > 122:
            nueva_cad = nueva_cad + i
        elif ord(i) < 97:
            nueva_cad = nueva_cad + chr(ord(i) + 32)
        else:
            nueva_cad = nueva_cad + chr(ord(i) - 32)

    print(nueva_cad)
    return nueva_cad


if __name__ == '__main__':

    # Intercambiar may-min en una palabra solo mayuscula
    intercambiar_mayusculas_minusculas("HOLA")
    # Intercambiar may-min en una palabra solo minuscula
    intercambiar_mayusculas_minusculas("hola")
    # Intercambiar may-min en una palabra con mayusculas y minusculas
    intercambiar_mayusculas_minusculas("HoLa")
    # Intercambiar may-min en una cadena con espacios
    intercambiar_mayusculas_minusculas("HoLa MunDO")
    # Intercambiar may-min en una cadena con otros caracteres
    intercambiar_mayusculas_minusculas("HoLa MunDO!! :) {}")
