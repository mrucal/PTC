# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:03:11 2017

@author: Mario
"""


def contar_letras(cad):

    lista = []
    letras = []

    for i in cad:
        if i not in letras:
            letras += [i]
            lista.append(tuple([i, cad.count(i)]))

    return lista


def contar_letras2(cad):

    lista = []

    for i in cad:
        encontrado = False
        for j in range(len(lista)):
            if lista[j][0] == i:
                encontrado = True
                lista[j] = tuple([i, lista[j][1] + 1])
                break
        else:
            if not encontrado:
                lista.append(tuple([i, 1]))

    return lista


if __name__ == '__main__':

    print(contar_letras('patata'))
    print(contar_letras2('patata'))
