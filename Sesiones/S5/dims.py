# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:11:07 2017

@author: Mario
"""


def dims(lista):

    if len(lista) == 0:
        return -1, -1

    for i in range(len(lista)):
        if type(lista[i]) == list:
            if len(lista[0]) != len(lista[i]):
                return -1, -1
        else:
            return -1, -1

    return len(lista), len(lista[0])


if __name__ == '__main__':

    print(dims([[3, 6, 4], [4, 9, 6]]))
    print(dims([[3, 6, 4, 2], [4, 9, 6]]))
    print(dims([[3, 6, 4]]))
    print(dims([[3], [4], [2]]))
    print(dims([]))
    print(dims([[]]))
    print(dims([[], []]))
    print(dims([[], [3]]))
    print(dims([['a', 'c', 'e'], ['1', 'abc', 'hola']]))
    print(dims([[[3, 6, 4], [3, 6, 4]], [[4, 9, 6], [4, 9, 6]]]))
    print(dims(['ab', 'cd']))
    print(dims([1, 2]))
