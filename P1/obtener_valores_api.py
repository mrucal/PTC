# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:42:34 2017

@author: Mario
"""

import urllib.request
import ssl
import xml.etree.ElementTree as ET
import json
import math


key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJydWNhbDJAaG90bWFpbC5jb20iLCJqdGkiOiI2MDgxNDM5NS03M2JmLTQyNjktYTFiMi1iMDA2YTJhMGFiNTQiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTUxMjkzMTU1MSwidXNlcklkIjoiNjA4MTQzOTUtNzNiZi00MjY5LWExYjItYjAwNmEyYTBhYjU0Iiwicm9sZSI6IiJ9.7z609ditZLGue_5GXFonIZtJTx3Rx14ZIVe8wnoGOAw'


def obtener_idema(provincia):
    
    provincia = provincia.upper()
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    url = urllib.request.urlopen('https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/?api_key='+key, context=ctx)
    contenido = json.loads(url.read().decode("utf-8","ignore"))
    
    url = urllib.request.urlopen(contenido['datos'], context = ctx)
    todas_estaciones = json.loads(url.read().decode("utf-8","ignore"))
    
    print('Elige una estación: ')
    estaciones_provincia = []
    for i in todas_estaciones:
        if provincia == i['provincia']:
            estaciones_provincia.append( i)
            print('\t- Estación:',i['nombre'])#,'\n\t\t- idema:',i['indicativo'],'\n')
            
    estacion = str(input()).upper()
    
    while True:
        for i in estaciones_provincia:
            if estacion == i['nombre']:
                estacion_nombre = i['nombre'][0] + i['nombre'][1:].lower()
                return i['indicativo'], estacion_nombre
        else:
            print ('No se encuentra la estacion '+ estacion +'. Introduce una estacion:')
            estacion = str(input()).upper()


def obtener_datos_estacion(idema):
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    url = urllib.request.urlopen('https://opendata.aemet.es/opendata/api/observacion/convencional/datos/estacion/'+idema+'/?api_key='+key, context = ctx)
    contenido = json.loads(url.read().decode("utf-8","ignore"))
    
    url = urllib.request.urlopen(contenido['datos'], context = ctx)
    contenido = json.loads(url.read().decode("utf-8","ignore"))
    
    try:
        if contenido['estado'] == 404:
            return -1
    except:
        pass
    
    return contenido


def obtener_hora_UTC(datos):
    try:
        return datos[-1]['fint']
    except:
        return '-'
    

def obtener_temperatura(datos):
    try:
        return datos[-1]['ta']
    except:
        return '-'


def obtener_humedad(datos):
    try:
        return datos[-1]['hr']
    except:
        return '-'
    

def obtener_punto_rocio(t, h):
    return round(((h/100)**(1/8)*(112 + 0.9 * t)) + (0.1 * t) - 112, 1)



def obtener_viento(datos):
    try:
        return datos[-1]['vmax']
    except:
        return '-'

def grado_a_cardinal(g):
    
    if g == 360 or (g >=0 and g < 22.5):
        return 'N'
    if g >= 22.5 and g < 45:
        return 'NNE'
    if g >= 45 and g < 67.5:
        return 'NE'
    if g >= 67.5 and g < 90:
        return 'ENE'
    if g >= 90 and g < 112.5:
        return 'E'
    if g >= 112.5 and g < 135:
        return 'ESE'
    if g >= 135 and g < 157.5:
        return 'SE'
    if g >= 157.5 and g < 180:
        return 'SSE'
    if g >= 180 and g < 202.5:
        return 'S'
    if g >= 202.5 and g < 225:
        return 'SSO'
    if g >= 225 and g < 247.5:
        return 'SO'
    if g >= 247.5 and g < 270:
        return 'OSO'
    if g >= 270 and g < 292.5:
        return 'O'
    if g >= 292.5 and g < 315:
        return 'ONO'
    if g >= 315 and g < 337.5:
        return 'NO'
    if g >= 337.5 and g < 360:
        return 'NNO'


def obtener_direccion_viento(datos):
    try:
        return grado_a_cardinal(datos[-1]['dmax'])
    except:
        return '-'
    

def obtener_viento_10(datos):
    try:
        return datos[-1]['vv']
    except:
        return '-'


def obtener_direccion_viento_10(datos):
    try:
        return grado_a_cardinal(datos[-1]['dv'])
    except:
        return '-'


def obtener_barometro(datos):
    try:
        return datos[-1]['pres']
    except:
        return '-'
    
    

def obtener_datos_hoy(datos):
    
    datos_hoy = []
    
    try:
        for i in datos:
            if i['fint'][:10] == datos[-1]['fint'][:10]:
                datos_hoy.append(i)

        return datos_hoy
    except:
        return datos_hoy
        
def obtener_lluvia_hoy(datos):
    try:
        precipitacion_hoy = 0
        datos_hoy = obtener_datos_hoy(datos)
        for i in datos_hoy:  
            precipitacion_hoy+=i['prec']
        return precipitacion_hoy
    except:
        return '-'
    
    
def obtener_intensidad_lluvia(datos):
    try:
        precipitacion = 0
        for i in datos:
            precipitacion+=i['prec']
        return round(precipitacion/24,1)
    except:
        return '-'
    

def obtener_indice_calor(t,h):
    
    # Temperatura en Farenheit
    tf = (t * 1.8) + 32
    #print('f:',t,tf)

    icf=  - 42.379 + 2.04901523*tf + 10.14333127*h - 0.22475541*tf*h - 6.83783*(10**-3)*(tf**2) - 5.481717*(10**-2)*(h**2) + 1.22874*(10**-3)*(tf**2)*h  + 8.5282*(10**-4)*tf*(h**2) - 1.99*(10**-6)*(tf**2)*(h**2)  
    #icf = 0.5 * (tf + 61.0 + ((tf - 68.0) * 1.2) + (h * 0.094))
   
    
    #print('c:',icf,(icf-32)*1.8,(((icf-32)*1.8) * 1.8) + 32)
    # En centigrados
    return round((icf-32)/1.8,1)
    

def obtener_sensacion_termica(t,vv):

    return round(33 + (t-33)*(0.474 + (0.454*math.sqrt(vv/3.6)) - 0.0454*vv/3.6),1)


def obtener_parametro_max_hoy(datos, parametro):
    
    try:
        
        datos_hoy = obtener_datos_hoy(datos)
        tmax = datos_hoy[0][parametro]
        
        for i in datos_hoy:
            if i[parametro] > tmax:
                tmax = i[parametro]
            
        return tmax
    
    except:
        return '-'
    
def obtener_parametro_min_hoy(datos, parametro):
    
    try:
        
        datos_hoy = obtener_datos_hoy(datos)
        tmin = datos_hoy[0][parametro]

        for i in datos_hoy:
            if i[parametro] < tmin:
                tmin = i[parametro]
            
        return tmin
    
    except:
        return '-'
    

def obtener_ic_st_max_hoy(datos):
    
    try:
        
        datos_hoy = obtener_datos_hoy(datos)
        ic = []
        st = []
        for i in datos_hoy:
            ic.append(obtener_indice_calor(i['ta'],i['hr']))
            st.append(obtener_sensacion_termica(i['ta'],i['vv']))
            
        return max(ic), max(st)
    
    except:
        return '-'
    
    
if __name__ == '__main__':
    
    import generar_html as gh

    idema = obtener_idema('cantabria')[0]#,'5530E')
    datos = obtener_datos_estacion(idema)
    #print('datos:',datos)
    print('hora:',obtener_hora_UTC(datos))
    t = obtener_temperatura(datos)
    print('temperatura:', t)
    h = obtener_humedad(datos)
    print('humedad:', h)
    print('punto de rocio:',obtener_punto_rocio(t, h))
    vv = obtener_viento(datos)
    print('viento:',vv)
    print('direccion viento:',obtener_direccion_viento(datos))
    print('viento:',obtener_viento_10(datos))
    print('direccion viento:',obtener_direccion_viento_10(datos))
    print('barometro:',obtener_barometro(datos))
    print('precipitacion hoy:',obtener_lluvia_hoy(datos))
    print('intesidad lluvia:', obtener_intensidad_lluvia(datos))
    
    
    
    print('indice de calor:',obtener_indice_calor(t,h))
    print('sensacion termica:',obtener_sensacion_termica(t,vv))
    print('temperatura max:', obtener_parametro_max_hoy(datos,'ta'))
    print('temperatura min:', obtener_parametro_min_hoy(datos,'ta'))
    print('humdedad max:', obtener_parametro_max_hoy(datos,'hr'))
    print('humdedad min:', obtener_parametro_min_hoy(datos,'hr'))
    gh.valores['t_val'] = '356.2º'
    gh.crear_html('test')
