# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:25:18 2017

@author: Mario
"""


def contar_letras(cad, letra):
    """ Cuenta el numero de apariciones de una letra en una cadena"""

    n = 0
    for i in cad:
        if i == letra:
            n += 1
    print(n)
    return n


if __name__ == '__main__':

    # La cadena es vacia
    contar_letras("", "o")
    # La letra no se encuentra en la cadena
    contar_letras("hola mundo!", "i")
    # La letra se encuentra una vez
    contar_letras("hola mundo!", "l")
    # La letra se encuentra mas de una vez
    contar_letras("hola mundooo!", "o")
