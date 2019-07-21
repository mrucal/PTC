# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 06:44:21 2017

@author: Mario
"""


import random


def mezclar1(l1, l2):
    res = l1 + l2
    res.sort()
    return res


def mezclar2(l1, l2):
    ''' Devuelve una nueva lista ordenada que mezcla dos listas ordenadas'''
    res = []
    i = 0
    j = 0
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res += [l1[i]]
            i += 1
        else:
            res += [l2[j]]
            j += 1

    if  i!= j:
        if i == len(l1)-1:
            res += l1[i:]
        else:
            res += l2[j:]

    return res


def esta_ordenada(res):

    for i in range(len(res)-1):
        if res[i] > res[i+1]:
            return False    

    return True#len(res) == len(l1) + len(l2)


def generar_lista_aleatoria_ordenada():

    l = [random.randint(0, 150) for i in range(random.randint(0, 30))]
    
    l = list(set(l))
    
    l.sort()

    return l


if __name__ == '__main__':
    
    if esta_ordenada(mezclar2([1, 3, 4, 6], [2, 5])):
        print('Lista correcta.')
    else:
        print('Lista incorrecta.')
    if esta_ordenada(mezclar2([1, 3, 4, 6], [2, 5, 7, 8])):
        print('Lista correcta.')
    else:
    	print('Lista incorrecta.')
    if esta_ordenada(mezclar2([2, 5], [1, 3, 4, 6])):
    	print('Lista correcta.')
    else:
    	print('Lista incorrecta.')
    if esta_ordenada(mezclar2([1, 2], [3, 4, 5, 6])):
    	print('Lista correcta.')
    else:
    	print('Lista incorrecta.')
    if esta_ordenada(mezclar2([], [1, 3, 4, 6])):
    	print('Lista correcta.')
    else:
    	print('Lista incorrecta.')
    if esta_ordenada(mezclar2([1, 3, 4, 6], [])):
    	print('Lista correcta.')
    else:
    	print('Lista incorrecta.')
    if esta_ordenada(mezclar2([], [])):
    	print('Lista correcta.')
    else:
    	print('Lista incorrecta.')
    
    fallos = False
    for i in range(20):
        l1 = generar_lista_aleatoria_ordenada()
        l2 = generar_lista_aleatoria_ordenada()
        res = mezclar2(l1, l2)
        if(not esta_ordenada(res)):
            print('Lista no ordenada:', res, l1, l2)
            fallos = True
    else:
        if not fallos:
            print('Todos correctos.')
        else:
            print('Hay errores.')
