# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:18:58 2018

@author: Mario
"""

from lxml import etree as et
import os


def obtener_nombre_automatico():
    
    # Obtener la lista de test que se han creado previamente con nombre automático
    auto = [i for i in os.listdir('tests/') if i[:6] == '_test_'  ]
    # Asignar nombre, que será el último creado más 1
    nombre = '_test_{:03d}'.format(len(auto)+1)
    for i in range(len(auto)):
        # Si falta algun número intermedio, devolverl
        if auto[i] != '_test_{:03d}.xml'.format(i+1):
            return '_test_{:03d}'.format(i+1)
            
    return nombre

def generar_test(nombre,preguntas, resultados = False, realizado=False, tipos=None, respuestas=None):
    
    test = et.Element('test')
    root = et.ElementTree(test)

    pi = 0
    for p in preguntas:
        
        pregunta = et.Element('pregunta')
        pregunta.attrib['id'] = str(pi+1)
        test.append(pregunta)
        
        pregunta.append(et.Element('enunciado'))
        pregunta[0].text = p['enunciado']
        
        indice = 1
        # Para incluir la valoración de la pregunta
        if resultados:
            pregunta.append(et.Element('valoracion'))
            pregunta[indice].text = str(p['valoracion'])
            indice += 1
        
        # Indicar el tipo de pregunta, si se está realizando el test
        if realizado:
            pregunta.append(et.Element('tipo'))
            pregunta[indice].text = str(tipos[pi])
            
        opciones = et.Element('opciones')
        pregunta.append(opciones)
        oi = 0
        for o in p['opciones']:
            
            opcion = et.Element('opcion')
            opcion.attrib['id'] = str(oi+1)
            opciones.append(opcion)
            
            opcion.append(et.Element('texto'))
            if resultados:
                opcion.append(et.Element('puntuacion'))
            
            if not realizado:
                opcion[0].text = o[0]
            else:
                opcion[0].text = o
            if resultados:
                opcion[1].text = str(o[1])
            
            oi+=1
            
        if realizado:
            respuestas_xml = et.Element('respuestas')
            pregunta.append(respuestas_xml)
            if tipos[pi] == 'multiple':
                    
                for rm in respuestas[pi]:
                    respuesta_xml = et.Element('respuesta')
                    respuestas_xml.append(respuesta_xml)
                    respuesta_xml.text=str(rm)
            else:
                respuesta_xml = et.Element('respuesta')
                respuestas_xml.append(respuesta_xml)
                respuesta_xml.text = str(respuestas[pi])
        
        pi+=1
        
    root.write(nombre+'.xml')
    
    
def leer_test_xml(nombre, resultados = False):
    
    xml = et.parse(nombre+'.xml')
    root = xml.getroot()
    test = []
    
    for pi_xml in root.findall('pregunta'):
        pi = {}
        if resultados:
            pi['valoracion'] = pi_xml.find('valoracion').text
        pi['enunciado'] = pi_xml.find('enunciado').text
        pi['opciones'] = []
        for o in pi_xml.find('opciones').findall('opcion'):
            if resultados:
                pi['opciones'].append((o[0].text,o[1].text))
            else:
                pi['opciones'].append(o[0].text)
        test.append(pi)
    
    return test

    
def leer_valoraciones_puntuaciones(nombre):
    
    xml = et.parse('tests_resueltos/'+nombre+'_resuelto.xml')
    root = xml.getroot()
    
    valoraciones = []
    puntuaciones = []
    for pi_xml in root.findall('pregunta'):
    
        valoraciones.append(float(pi_xml.find('valoracion').text))
        
        puntuaciones_i = []
        for o in pi_xml.find('opciones').findall('opcion'):
            puntuaciones_i.append(int(o[1].text))
        puntuaciones.append(puntuaciones_i)
    
    return valoraciones,puntuaciones


def leer_tipos_respuestas(nombre_test,nombre_realizador):
    
    xml = et.parse('tests_realizados/'+nombre_test+'_'+nombre_realizador+'.xml')
    root = xml.getroot()
    
    tipos = []
    respuestas = []
    for pi_xml in root.findall('pregunta'):
        tipo = pi_xml.find('tipo').text
        tipos.append(tipo)
        if tipo == 'multiple':
            multiple = []
            for m in pi_xml.find('respuestas').findall('respuesta'):
                multiple.append(int(m.text))
            respuestas.append(multiple)
        else:
            respuestas.append(int(pi_xml.find('respuestas').find('respuesta').text))
        
    return tipos,respuestas


if __name__ == '__main__':
    '''preguntas = [{'valoracion': 1, 'enunciado': 'enunciado 1', 'opciones': [('o1_1', 1), ('o1_2', 451)]},{'valoracion': 2, 'enunciado': 'enunciado 2', 'opciones': [('o2_1', 824), ('o2_2', 498)]}]
    generar_test('test_resuelto', preguntas, respuestas = True)
    generar_test('test_to_do', preguntas)
    
    nombre=obtener_nombre_automatico()
    generar_test('tests/'+nombre,preguntas)
    generar_test('tests_resueltos/'+nombre+'_resuelto',preguntas)'''

    #leer_test_xml('tests/prueba')
    print(leer_valoraciones_puntuaciones('prueba'))
    print(leer_tipos_respuestas('prueba','mario'))
    #print(leer_test_resuelto_xml('tests_resueltos/prueba_resuelto'))