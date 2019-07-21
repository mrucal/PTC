# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 07:51:31 2017

@author: Mario
"""


def eliminar(l1, l2):

    for i in l2:
        while i in l1:
            l1.remove(i)


def comprueba(l1, l2):

    eliminar(l1, l2)

    for i in l2:
        if i in l1:
            return False

    return True


if __name__ == '__main__':

    print(comprueba([1, 5, 5, 5, 3, 5], [5]))
