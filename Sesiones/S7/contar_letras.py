# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:06:56 2017

@author: Mario
"""

import random
import time
random.seed(time.time())

def genera_cadena_ADN(n):
    
    cad='ACTG'
    
    adn = ""
    
    for i in range(n):
        adn += cad[random.randint(0,3)]
    
    return adn


def contar_letras(cadena):
    
    t_inicio = time.time()
    res = {}
    for i in cadena:
        try:
            res[i] += 1
        except:
            res[i] = 1
    
    t_total = time.time() - t_inicio;
    return res,format(t_total,'.30f')
        
def contar_letras_lista(cadena):
    
    t_inicio = time.time()
    res = []
    encontrado = False
    for i in cadena:
        for j in range(len(res)):
            encontrado=False
            if i == res[j][0]:
                
                res[j] = (res[j][0], res[j][1]+1)
                encontrado=True
                break;
        else:
            if not encontrado:
                res.append((i,1))
                
    t_total = time.time() - t_inicio;
    return res,format(t_total,'.30f')

def genera_numeros(n,rango):
        
    numeros = ""
    
    for i in range(n):
        numeros += str(random.randint(0,rango))
    
    return numeros

def diccionario_inverso(dic):
    
    inverso = {}
    
    for i in dic:
        try:
            inverso[dic[i]].append(i)
        except:
            inverso[dic[i]] = [i]
            
    return inverso

def obtener_diccionario_inverso(inverso):
    
    dic = {}
    
    for i in inverso:
        for j in inverso[i]:
            dic[j]=i
 
            
    return dic
                
        
        
if __name__ == '__main__':
    
    adn = genera_cadena_ADN(10000)
    print(contar_letras(adn))
    print(contar_letras_lista(adn))
    
    numeros = genera_numeros(100000,10000)
    print(contar_letras(numeros))
    print(contar_letras_lista(numeros))
    
    print()
    cad = genera_numeros(20,10)
    dic,t = contar_letras(cad)
    print(dic)
    dic_inverso=diccionario_inverso(dic)
    print(dic_inverso)
    dic_original=obtener_diccionario_inverso(dic_inverso)
    print(dic_original)
    