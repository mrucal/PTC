# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:39:47 2017

@author: Mario
"""
 
from tkinter import *
from tkinter.messagebox import *
import os

import añadir_editar_pregunta as ap
import gestionar_xml as gx


root = None
preguntas = []
listbox = None
nombre_label = None


def añadir():
    
    global root
    global preguntas
    global listbox
    
    # Abir nueva ventana. 
    ventana_añadir_pregunta = Toplevel()    
    ventana_añadir_pregunta.transient(master=root)    
    ventana_añadir_pregunta.grab_set()
    
    ap.añadir_editar_pregunta(ventana_añadir_pregunta)
    
    # No se podrá acceder a la ventana actual hasta que no se cierre la nueva.
    root.wait_window(ventana_añadir_pregunta)
    
    try:
        preguntas.append(ap.pregunta)
        # Mostrar la pregunta en el listbox
        if len(ap.pregunta['enunciado']) >= 20:
            listbox.insert(END,str(listbox.size()+1)+'.-'+ap.pregunta['enunciado'][:20]+'...')
        else:
            listbox.insert(END,str(listbox.size()+1)+'.-'+ap.pregunta['enunciado'])
    except:
        # Si se ha cerrado la ventana para añadir una pregunta, sin aceptar la pregunta
        preguntas = []


def editar():
    
    global root
    global preguntas
    global listbox
    
    error = False
    
    try:
        i = listbox.curselection()[0]
    except:
        showinfo(title='ERROR',message='No has seleccionado ninguna pregunta.')
        error = True
    
    if not error:
        
        # Abir nueva ventana. 
        ventana_añadir_pregunta = Toplevel()    
        ventana_añadir_pregunta.transient(master=root)    
        ventana_añadir_pregunta.grab_set()

        ap.añadir_editar_pregunta(ventana_añadir_pregunta, preguntas[i])
        
        # No se podrá acceder a la ventana actual hasta que no se cierre la nueva.
        root.wait_window(ventana_añadir_pregunta)
        
        try:
            # Modificar la pregunta editada
            preguntas[i]=ap.pregunta
            # Mostrar el cambio en el listbox, eliminando la pregunta antigua e insertando la nueva
            if len(ap.pregunta['enunciado']) >= 20:
                listbox.delete(i)
                listbox.insert(i,str(i+1)+'.-'+ap.pregunta['enunciado'][:20]+'...')
            else:
                listbox.delete(i)
                listbox.insert(i,str(i+1)+'.-'+ap.pregunta['enunciado'])
        except:
            # Si se ha cerrado la ventana sin editar la pregunta no se hace nada
            pass


def aceptar():
    
    global root
    global preguntas
    global nombre_test
    global nombre_label
    
    if len(preguntas) == 0:
        showinfo(title='ERROR',message='Debe haber alguna pregunta.')
    else:
        
        nombre_test = nombre_label.get()
        
        try:
            os.stat('tests/')
        except:
            os.mkdir('tests/')
        
        try:
            os.stat('tests_resueltos/')
        except:
            os.mkdir('tests_resueltos/')
        
        # Si no se ha indicado un nombre al test, se le asigna uno automático
        if nombre_test == '':
            nombre_test = gx.obtener_nombre_automatico()
        
        # Crear los xml, con el test completo resuelto, y sin las valoraciones
        gx.generar_test('tests_resueltos/'+nombre_test+'_resuelto', preguntas, resultados = True)
        gx.generar_test('tests/'+nombre_test, preguntas)
        
        # Obtener las valoraciones de cada pregunta
        valoraciones, p= gx.leer_valoraciones_puntuaciones(nombre_test)
        
        val_total = 0
        for i in valoraciones:
            val_total += i
        
        # Si las valoraciones no suman 10 puntos, no se puede crear el test
        if val_total == 10:
            root.destroy()
        else:
            showinfo(title='ERROR',message='Las valoraciones de cada pregunta deben sumar 10.')


def crear_test():
    
    global root
    global listbox
    global nombre_label
        
    root = Tk()
    
    root.title('Crear Test')
    root.geometry('365x310')
    root.resizable(False, False)
    
    Label(root, text = 'Crear nuevo test:')
    
    Label(root, text = 'Nombre del test:').place(x=20,y=10)    
    nombre_label = Entry(root)
    nombre_label.place(x=120,y=10)
    
    panel = LabelFrame(root,bg = '#DADADA', text = 'Preguntas:')
    panel.place(x=20,y=45) 
    
    listbox = Listbox(panel, activestyle=NONE, width = 50, height = 10)
    listbox.grid(row=0,column=0)
    scrollBarY = Scrollbar(panel, orient=VERTICAL, command=listbox.yview)
    scrollBarY.grid(row=0,column=1,sticky=N+S)
    listbox.config(yscrollcommand = scrollBarY.set)
    
    Button(root, text="Añadir", command = añadir, width=6).place(x=292,y=235)
    Button(root, text="Editar", command = editar, width=6).place(x=230,y=235)
    Button(root, text="Aceptar", command = aceptar, width=6).place(x=292,y=270)    
    
    root.mainloop()  
    
if __name__ == '__main__':
    crear_test()