# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:26:19 2017

@author: Mario
"""


def eliminar_letra(cad, letra):
    """ Eliminar todas las apariciones de una letra en una cadena"""

    nueva_cad = ""

    for i in cad:
        if i != letra:
            nueva_cad = nueva_cad + i

    print(nueva_cad)
    return nueva_cad


if __name__ == '__main__':

    # La cadena es vacia
    eliminar_letra("", "o")
    # La letra no se encuentra en la cadena
    eliminar_letra("hola mundo!", "i")
    # La letra se encuentra una vez
    eliminar_letra("hola mundo!", "l")
    # La letra se encuentra mas de una vez
    eliminar_letra("hola mundooo!", "o")
