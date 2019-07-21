# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 07:26:31 2017

@author: Mario
"""


import dims


def traspuesta(lista):

    dim = dims.dims(lista)

    if dim == (-1, -1):
        return []

    res = []
    for i in range(dim[1]):
        res.append([lista[j][i] for j in range(dim[0])])

    return res


def es_traspuesta(l1, l2):

    dim1 = dims.dims(l1)
    dim2 = dims.dims(l2)

    if dim1 == (-1, -1) or dim2 == (-1, -1) or dim1[0] != dim2[1] or dim1[1] != dim2[0]:
        return False
    
    for i in range(dim1[0]):
        for j in range(dim1[1]):
            if l1[i][j] != l2[j][i]:
                return False
    
    return True

        
if __name__ == '__main__':

    print(traspuesta([[3, 6, 4], [4, 9, 6]]))
    print(es_traspuesta([[3, 6, 4], [4, 9, 6]],traspuesta([[3, 6, 4], [4, 9, 6]])))
    print(traspuesta([[3, 4], [4, 9, 6]]))
    print(traspuesta([[3, 6, 4]]))
    print(traspuesta([[3]]))
