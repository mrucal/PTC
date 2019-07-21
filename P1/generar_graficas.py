# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:19:52 2017

@author: Mario
"""


import guardar_datos as gd

from datetime import datetime, date, time, timedelta
import matplotlib.pyplot as plt
import os


def obtener_param_7_dias(datos_json,param):
    
    #print(datos_json)
    
    hora_act = datetime.now().utcnow()
    a = str(hora_act)[:4]
    m = str(hora_act)[5:7]
    
    dias = list(datos_json[a][m])
    
    d = -7
    while(True):
        try:
            dias[d]
            break
        except:
            d = d + 1

    param_dias = []
    for i in range(d,0):
        param_i = 0
        for h in datos_json[a][m][dias[i]]:
            param_i += datos_json[a][m][dias[i]][h][param]
        param_dias.append(round(param_i/len(datos_json[a][m][dias[i]]),1))

    return param_dias,[str(dias[i])+'-'+str(m)+'-'+str(a) for i in range(d,0)]


def dibuja(nombre,param_vals, dias,param_nombre):
    
    #print (param_vals)
    plt.figure() 
    
    plt.title(param_nombre) 
    plt.xlabel(param_nombre)
    plt.xticks(range(len(dias)),dias)
    plt.plot(param_vals) 
    
    try:
        os.stat('html/graficos/')
    except:
        os.mkdir('html/graficos/')   
        
    plt.savefig('html/graficos/'+nombre+'.png')
    
if __name__ == '__main__':
    
    datos_json = gd.leer_datos('Granada-Loja')
    
    
    print(obtener_param_7_dias(datos_json,'t'))
    print(obtener_param_7_dias(datos_json,'hr'))
    print(obtener_param_7_dias(datos_json,'bar'))
    print(obtener_param_7_dias(datos_json,'v'))
    
    t, t_dias = obtener_param_7_dias(datos_json,'t')
    hr, hr_dias = obtener_param_7_dias(datos_json,'hr')
    bar, bar_dias = obtener_param_7_dias(datos_json,'bar')
    v, v_dias = obtener_param_7_dias(datos_json,'v')
    
    dibuja('T',t,t_dias,'Temperatura')
    dibuja('H',hr,hr_dias,'Humedad')
    dibuja('B',bar,bar_dias,'Barómetro')
    dibuja('V',v,v_dias,'Viento')