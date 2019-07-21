# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:46:50 2017

@author: Mario
"""


def trocear(cad, num):

    lista = []

    for i in range(0, len(cad), num):
        lista += [cad[i:i+num]]

    return lista


if __name__ == '__main__':

    # 1 Cadena vacía: []
    print("1.", trocear("", 5))

    # 2 num = longitud cad : ['Hola mundo']
    print("2.", trocear("Hola mundo", 10))

    # 3 num > longitud cad : ['Hola mundo']
    print("3.", trocear("Hola mundo", 13))

    # 4 num multiplo longitud cad : ['Ho', 'la', ' m', 'un', 'do']
    print("4.", trocear("Hola mundo", 2))

    # 5 num NO multiplo longitud cad : ['Hol', 'a m', 'und', 'o']
    print("5.", trocear("Hola mundo", 3))

    # 6 num NO multiplo longitud cad : ['Hola', ' mun', 'do']
    print("6.", trocear("Hola mundo", 4))
