# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:42:34 2017

@author: Mario
"""

import urllib.request
import xml.etree.ElementTree as ET

def obtener_xml(codigo_localidad):

    url = urllib.request.urlopen('http://www.aemet.es/xml/municipios/localidad_' + str(codigo_localidad) + '.xml')
    contenido = url.read()
    xml = ET.fromstring(contenido)
    
    return xml

def obtener_localidad_provincia(root):
    return root[2].text, root[3].text

def obtener_dias(root):
    return root[4]


def obtener_temperatura(dia):
    t = dia.find('temperatura')
    temperatura = {'maxima': t[0].text, 'minima': t[1].text, 'dato': [i.text for i in t.findall('dato')]}
    return temperatura


'''18087'''
if __name__ == '__main__':

    import generar_html as gh
    
    root = obtener_xml(18188)

    localidad = obtener_localidad_provincia(root)
    print(localidad[0] + ',', localidad[1])

    dias = obtener_dias(root)
    '''
    for dia in dias:
        print('temperatura', dia.attrib['fecha'] + ':', obtener_temperatura(dia))
    '''
    
    gh.valores['t_val'] = '356.2º'
    gh.crear_html('prueba')
