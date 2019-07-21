# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:52:39 2017

@author: Mario
"""


def es_inversa(cad1, cad2):

    """if len(cad1) != len(cad2):
        print(False)
        return False
    """
    print(cad1 == cad2[::-1])
    return cad1 == cad2[::-1]


if __name__ == '__main__':

    es_inversa("hola mundo", "odnum aloh")
