# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 20:35:18 2017

@author: Mario
"""

import json
import os
    
def guardar_datos(nombre,datos):
    
    try:
        with open('json/'+nombre+'.json', 'r',encoding='utf-8') as file:
            datos_json = json.load(file)
    except:
        datos_json = {}
    for i in datos:
        
        a = i['fint'][:4]
        m = i['fint'][5:7]
        d = i['fint'][8:10]
        h = i['fint'][11:]
        
        try:
            escribir = {'t': i['ta']}
        except:
            escribir = {'t': 0}
        try:
            escribir['hr'] = i['hr']
        except:
            escribir['hr'] = 0
        try:
            escribir['bar'] = i['pres']
        except:
            escribir['bar'] = 0
        try:
            escribir['v'] = i['vmax']
        except:
            escribir['v'] = 0   
            
            
        try:
            datos_json[a][m][d][h] = escribir
        except:
            try:
                datos_json[a][m][d] = {h:escribir}
            except:
                try:
                    datos_json[a][m] = {d:{h:escribir}}
                except:
                    datos_json[a] = {m:{d:{h:escribir}}}
    
    try:
        os.stat('json/')
    except:
        os.mkdir('json/')   
    
    with open('json/'+nombre+'.json','w',encoding='utf-8') as file:
        json.dump(datos_json,file)

def leer_datos(nombre):
    
    try:
        with open('json/'+nombre+'.json', 'r',encoding='utf-8') as file:
            datos = json.load(file)
            return datos
    except:
        return []