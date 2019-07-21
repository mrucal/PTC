# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:58:25 2017

@author: Mario
"""


def contar_pares(lista):

    pares = 0

    for i in lista:
        if type(i) == int and i % 2 == 0:
            pares += 1

    return pares


if __name__ == '__main__':

    # Lista vacia
    print(contar_pares([]))

    # Lista de numeros impares
    print(contar_pares([[5, 7, 11]]))

    # Lista de solo numeros con 4 pares
    print(contar_pares([0, 2, 5, 7, 78, 11, 96]))

    # Lista de numeros y otros tipos con 4 pares
    print(contar_pares([0, 2, 'hola', 5, 7, 78, 11, True, 96]))
