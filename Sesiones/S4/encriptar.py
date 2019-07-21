# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:00:01 2017

@author: Mario
"""

def encriptar_sin_espacios(texto, pos):
    """ Sin tener en cuenta espacios y otros caracteres"""
    texto = texto.lower()
    pos %= 26

    return ''.join([chr((ord(i) - 97 + pos) % 26 + 97) for i in texto])



def encriptar(texto, pos):
    """ Manteniendo espacios y otros caracteres"""
    texto = texto.lower()
    pos %= 26

    encriptado = ""
    for i in texto:
        if ord(i) >= 97 and ord(i) <= 122:
            encriptado += chr((ord(i) - 97 + pos) % 26 + 97)
        else:
            encriptado += i

    return encriptado



def desencriptar(texto, pos):

    return encriptar(texto, -pos)


if __name__ == '__main__':

    # Prueba con el alfabeto
    print(encriptar('abcdefghijklmnopqrstvwxyz', 5))
    print(desencriptar('fghijklmnopqrstuvwxyabcde', 5))

    # Prueba con una texto
    print(encriptar('Hola', 15))
    print(desencriptar('wdap', 15))
    
    # Prueba con una texto
    print(encriptar('Hola mundo', 22))
    print(desencriptar('dkhw iqjzk', 22))

    print(encriptar_sin_espacios('Hola mundo', 22))
    print(desencriptar('dkhwjiqjzk', 22))