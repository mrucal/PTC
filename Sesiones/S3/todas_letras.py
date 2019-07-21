# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:13:03 2017

@author: Mario
"""


def todas_letras(texto, letras):

    texto = texto.lower()
    letras = letras.lower()

    for i in letras:
        if texto.find(i) == -1:
            return False

    return True


if __name__ == '__main__':

    # 1 texto vacío, letras vacío : Correcto
    if todas_letras("", ""):
        print("1. Correcto")
    else:
        print("1. Incorrecto")

    # 2 texto vacío, letras no vacío : Incorrecto
    if todas_letras("", "ab"):
        print("2. Correcto")
    else:
        print("2. Incorrecto")

    # 3 un carecter: Incorrecto
    if todas_letras("a", "ab"):
        print("3. Correcto")
    else:
        print("3. Incorrecto")

    # 4 encuentra todas las letras desordenadas: Correcto
    if todas_letras("cgbad", "ab"):
        print("4. Correcto")
    else:
        print("4. Incorrecto")

    # 5 no estan todas las letras: Incorrecto
    if todas_letras("QWAEfw", "ab"):
        print("5. Correcto")
    else:
        print("5. Incorrecto")

    # 5b algunas letras en mayuscula: Correcto
    if todas_letras("QWAEfbw", "ab"):
        print("5b. Correcto")
    else:
        print("5b. Incorrecto")

    # 6 cuatro letras a buscar, estan todas en distinto orden:Correcto
    if todas_letras("peaicwBd", "abcd"):
        print("6. Correcto")
    else:
        print("6. Incorrecto")

    # 7 no hay letras a buscar: Correcto
    if todas_letras("abcd", ""):
        print("7. Correcto")
    else:
        print("7. Incorrecto")
