# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:29:44 2017

@author: Mario
"""


def suma_digitos(cad):

    suma = 0

    if type(cad) == str:
        for i in cad:
            # Ignora los caracteres distintos de numeros y suma solo los numeros
            if ord(i) >= 48 and ord(i) <= 57:
                suma += int(i)
    if type(cad) == int:
        suma = suma_digitos(str(cad))

    return suma


if __name__ == '__main__':

    # Suma digitos, con entrada tipo cadena y tipo entero
    print(suma_digitos('175'))
    print(suma_digitos(175))
    
    # Suma digitos, con entrada tipo cadena ignorando caracteres distintos de numeros
    print(suma_digitos('a1b7c5'))
