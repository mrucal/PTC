# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:21:54 2017

@author: Mario
"""

def hola(x='Hola mundo!!'):
    """ Función que escribe hola."""
    print(x)


# %%
hola()
# %%
x = 6
print(x)
# %%

if __name__ == '__main__':
    hola()
    import average
    y = average.average(23, 5)
    print(y)
