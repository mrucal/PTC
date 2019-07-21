# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:46:28 2017

@author: Mario
"""


def pangrama(texto):

    # Convertir mayusculas a minusculas
    texto = texto.lower()

    # Obtener todas las letras del alfabeto
    alfabeto = [chr(i) for i in range(97, 123)]

    # Eliminar caracteres distintos de letras
    texto_aux = ''
    for i in texto:
        if ord(i) >= 97 and ord(i) <= 122:
            texto_aux = texto_aux + i

    for i in alfabeto:
        if i not in texto_aux:
            return False

    return True


if __name__ == '__main__':
    
    # Cadena vacia
    print(pangrama(''))
    
    # Pangrama
    print(pangrama('Jose compro una vieja zampoa en Peru. Excusándose, Sofia tiro su whisky al desague de la banqueta.'))

    # No es pangrama
    print(pangrama('Hola mundo'))