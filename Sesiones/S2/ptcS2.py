# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:52:39 2017

@author: Mario
"""


def contar_letras(cad, letra):
    """ Cuenta el numero de apariciones de una letra en una cadena"""

    n = 0
    for i in cad:
        if i == letra:
            n += 1
    print(n)
    return n


def eliminar_letra(cad, letra):
    """ Eliminar todas las apariciones de una letra en una cadena"""

    nueva_cad = ""

    for i in cad:
        if i != letra:
            nueva_cad = nueva_cad + i

    print(nueva_cad)
    return nueva_cad


def intercambiar_mayusculas_minusculas(cad):
    """Intercambia letras mayusculas y minusculas en una cadena"""

    nueva_cad = ""

    for i in cad:
        if ord(i) < 64 or ord(i) > 122:
            nueva_cad = nueva_cad + i
        elif ord(i) < 97:
            nueva_cad = nueva_cad + chr(ord(i) + 32)
        else:
            nueva_cad = nueva_cad + chr(ord(i) - 32)

    print(nueva_cad)
    return nueva_cad


def buscar(cad, sub):
    """ Busca una subcadena en una cadena. Devuelve la posicion de la primera
    aparicion de la subcadena (si la subcadena esta en la cadena) y
    -1 en caso contrario"""

    if sub == "":
        print("-1")
        return -1

    n_sub = len(sub)

    for i in range(len(cad)-n_sub+1):
        if cad[i:i+n_sub] == sub:
            print(i)
            return i
    else:
        print(-1)
        return -1


def es_inversa(cad1, cad2):

    """if len(cad1) != len(cad2):
        print(False)
        return False
    """
    print(cad1 == cad2[::-1])
    return cad1 == cad2[::-1]


if __name__ == '__main__':

    """ Pruebas contar_letras
    # La cadena es vacia
    contar_letras("", "o")
    # La letra no se encuentra en la cadena
    contar_letras("hola mundo!", "i")
    # La letra se encuentra una vez
    contar_letras("hola mundo!", "l")
    # La letra se encuentra mas de una vez
    contar_letras("hola mundooo!", "o")
    """

    """ Pruebas eliminar_letra
    # La cadena es vacia
    eliminar_letra("", "o")
    # La letra no se encuentra en la cadena
    eliminar_letra("hola mundo!", "i")
    # La letra se encuentra una vez
    eliminar_letra("hola mundo!", "l")
    # La letra se encuentra mas de una vez
    eliminar_letra("hola mundooo!", "o")
    """

    """ Pruebas intercambiar_mayusculas_minsuculas
    # Intercambiar may-min en una palabra solo mayuscula
    intercambiar_mayusculas_minusculas("HOLA")
    # Intercambiar may-min en una palabra solo minuscula
    intercambiar_mayusculas_minusculas("hola")
    # Intercambiar may-min en una palabra con mayusculas y minusculas
    intercambiar_mayusculas_minusculas("HoLa")
    # Intercambiar may-min en una cadena con espacios
    intercambiar_mayusculas_minusculas("HoLa MunDO")
    # Intercambiar may-min en una cadena con otros caracteres
    intercambiar_mayusculas_minusculas("HoLa MunDO!! :) {}")"""

    """ Pruebas buscar cadena
    # La subcadena es vacia
    buscar("hola mundo", "")
    # La subcadena no esta en la cadena
    buscar("hola mundo", "Mundo")
    # La subcadena es un caracter
    buscar("hola mundo", "m")
    # La subcadena tiene mas de un caracter"
    buscar("hola mundo", "la")
    buscar("Hola Mundo", "Mundo")
    """

    """ Pruebas es_inversa
    es_inversa("hola mundo", "odnum aloh")"""
