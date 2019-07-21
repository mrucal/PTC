# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:27:51 2017

@author: Mario
"""


def buscar(cad, sub):
    """ Busca una subcadena en una cadena. Devuelve la posicion de la primera
    aparicion de la subcadena (si la subcadena esta en la cadena) y
    -1 en caso contrario"""

    if sub == "":
        print("-1")
        return -1

    n_sub = len(sub)

    for i in range(len(cad)-n_sub+1):
        if cad[i:i+n_sub] == sub:
            print(i)
            return i
    else:
        print(-1)
        return -1


if __name__ == '__main__':

    # La subcadena es vacia
    buscar("hola mundo", "")
    # La subcadena no esta en la cadena
    buscar("hola mundo", "Mundo")
    # La subcadena es un caracter
    buscar("hola mundo", "m")
    # La subcadena tiene mas de un caracter"
    buscar("hola mundo", "la")
    buscar("Hola Mundo", "Mundo")
