# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:15:54 2017

@author: Mario
"""


def ordenamientoBurbuja(unaLista):
    """
    devuelve la lista ordenada
    >>> ordenamientoBurbuja([])  
    []
    >>> ordenamientoBurbuja([54,26,93,17,77,31,44,55,20])  
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    >>> ordenamientoBurbuja([54,26,93,17,77,31,17,44,55,20])  
    [17, 17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
            	unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]
    return unaLista

if __name__ == '__main__':
    import doctest
    doctest.ELLIPSIS
    doctest.testmod(verbose = True, optionflags=doctest.ELLIPSIS)