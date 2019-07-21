# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:10:19 2017

@author: Mario
"""

def suma(a,b):
    
    """
    >>> suma(1,10)
    55
    """
    
    sum=0
    for i in range(a,b+1):
        sum += i
        
    return sum


if __name__ == '__main__':
    import doctest
    doctest.ELLIPSIS
    doctest.testmod(verbose = True, optionflags=doctest.ELLIPSIS)
    print(suma(1,10))