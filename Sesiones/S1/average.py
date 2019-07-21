# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:13:51 2017

@author: Mario
"""

def average(a, b):
    """
    Given two numbers a and b, return their average value.

    Parameters
    ----------
    a : number
     A number
    b : number
     Another number

    Return
    ------
    res : number
      The average of a and b, computed using 0.5 *(a + b)
    Example
    -------
    >>> average(5,10)
    7,5

    """

    return (a + b) * 0.5

if  __name__=='__main__':
    import hola
    print(average(12, 6))
