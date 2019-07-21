# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 18:15:11 2018

@author: Mario
"""

from tkinter import *
from tkinter.messagebox import *
import os

import gestionar_xml as gx
import realizar_test as rt
import corregir_test as ct

root = None
listbox = []

def aceptar():
    
    global root
    global preguntas
    global listbox
    global ls
    global corregir2
    
    error = False
    
    try:
        selections = listbox.curselection()
    except:
        showinfo(title='ERROR',message='No has seleccionado ningun test.')
        error = True
    
    if corregir2:
        k = len(ls[selections[0]]) - ls[selections[0]][::-1].index('_') - 1
        nombre_test_0 = ls[selections[0]][:k]
        nombre_realizador = []
        for i in selections:
            # Los ficheros con los resultados del test tienen el formato: test_nombre.xml
            # Calcular el indice del último '_', para obtener el nombre
            k = len(ls[i]) - ls[i][::-1].index('_') - 1
            nombre_test = ls[i][:k]
            nombre_realizador_i = ls[i][k+1:-4]
            nombre_realizador.append(nombre_realizador_i)
            if nombre_test_0 != nombre_test:
                showinfo(title='ERROR',message='No puedes elegir tests diferentes.')
                error = True
                
    if not error:
        root.destroy()

        if corregir2:
            valoraciones = []
            puntuaciones = []
            tipos = []
            respuestas = []
            
            for i in range(len(selections)): 
                valoraciones_i, puntuaciones_i = gx.leer_valoraciones_puntuaciones(nombre_test)
                tipos_i, respuestas_i = gx.leer_tipos_respuestas(nombre_test,nombre_realizador[i])
                
                valoraciones.append(valoraciones_i)
                puntuaciones.append(puntuaciones_i)
                tipos.append(tipos_i)
                respuestas.append(respuestas_i)
            
            ct.corregir_test(nombre_test, nombre_realizador, valoraciones, puntuaciones, tipos, respuestas)
        else:
            preguntas = gx.leer_test_xml('tests/'+ls[selections[0]][:-4])
            rt.realizar_test(ls[selections[0]][:-4],preguntas)


def abrir_test(corregir = False):
    
    global root
    global listbox
    global nombre_label
    global ls
    global corregir2
    
    corregir2 = corregir
    
    root = Tk()
    
    if corregir:
        root.title('Abrir Test Realizado')
    else:
        root.title('Abrir Test')
    
    root.geometry('365x235')
    root.resizable(False, False)
    
    if not corregir:
        try:
            os.stat('tests/')
        except:
            showinfo(title='ERROR',message='No hay tests disponibles.') 
    else:
        try:
            os.stat('tests_realizados/')
        except:
            showinfo(title='ERROR',message='No hay tests disponibles.') 
        
    if corregir:
        panel = LabelFrame(root,bg = '#DADADA', text = 'Tests Realizado (elige uno o varios):')
    else:
        panel = LabelFrame(root,bg = '#DADADA', text = 'Tests:')
    panel.place(x=20,y=10) 
    
    if corregir:
        listbox = Listbox(panel,selectmode = MULTIPLE, activestyle=NONE, width = 50, height = 10)
    else:
        listbox = Listbox(panel, activestyle=NONE, width = 50, height = 10)
    listbox.grid(row=0,column=0)
    scrollBarY = Scrollbar(panel, orient=VERTICAL, command=listbox.yview)
    scrollBarY.grid(row=0,column=1,sticky=N+S)
    listbox.config(yscrollcommand = scrollBarY.set)
    
    if not corregir:
        ls = os.listdir('tests/')
    else:
        ls = os.listdir('tests_realizados/')
        
    for i in ls:
        listbox.insert(END,i[:-4])
        
    Button(root, text="Aceptar", command = aceptar, width=6).place(x=292,y=200) 
    
    root.mainloop() 
    
if __name__ == '__main__':
    abrir_test(corregir=False)