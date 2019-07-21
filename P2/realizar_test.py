# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:23:00 2018

@author: Mario
"""


from tkinter import *
from tkinter.messagebox import *

respuestas = []

import gestionar_xml as gx
import os

def aceptar():
    
    global nombre
    global root
    global nombre_label
    global tipos
    global widgets
    global preguntas
    global respuestas
    
    error = False
    
    nombre_realizador = nombre_label.get()
    if nombre_realizador == '':
        showinfo(title='ERROR',message='Introduce tu nombre.')
        error = True
        
    if nombre_realizador.count('_') != 0:
        showinfo(title='ERROR',message='Tu nombre no puede contener el caracter "_".')
        error = True

    respuestas = []
    for i in range(len(tipos)):
        if tipos[i] != 'multiple':
            if widgets[i].get() != 0:
                respuestas += [widgets[i].get()-1]
            else:
                showinfo(title='ERROR',message='No has contestado a la pregunta {}.'.format(i+1)) 
                error = True
        else:
            respuestas_m = [w for w in range(len(widgets[i])) if widgets[i][w].get()!= 0]
            if len(respuestas_m) == 0:
                showinfo(title='ERROR',message='No has contestado a la pregunta {}.'.format(i+1)) 
                error = True
            if len(respuestas_m) == len(tipos):
                showinfo(title='ERROR',message='Pregunta {}: No puedes marcar todas las respuestas.'.format(i+1)) 
                error = True
            respuestas.append(respuestas_m)
    
    if not error:
        try:
            os.stat('tests_realizados/')
        except:
            os.mkdir('tests_realizados/')
        gx.generar_test('tests_realizados/'+nombre+'_'+nombre_realizador, preguntas, realizado=True,tipos=tipos,respuestas=respuestas)
        root.destroy()

def comprobar_tipo_opcion(opciones):
    
    positivas = [o for o in opciones if int(o[1]) > 0]
    
    if len(positivas) > 1:
        return 'multiple'
    
    negativas = [o for o in opciones if int(o[1]) < 0]
    
    if len(negativas) > 1:
        return 'penalizado'
    else:
        return 'no-penalizado'    
    
def update_scrollregion(event):
    global canvas
    canvas.configure(scrollregion=canvas.bbox("all"))
    
def opcion_multiple(root,pregunta,pi):
    
    global r
    
    pregunta_lf = LabelFrame(root,bg = '#DADADA', text = 'Pregunta {}:'.format(pi),font=("Arial 12 bold"))
    pregunta_lf.grid(row=r,column=0,padx=(10,10),pady=(10,10))
    
    enunciado = Label(pregunta_lf,bg='#DADADA',text = pregunta['enunciado'],font=("Arial 9 bold"), wraplength= 600, justify= LEFT, width = 84, height = 6, anchor = W)
    enunciado.grid(row=r,column=0,padx=(10,10))
    
    r += 1
    opciones_widget = []
    for o in pregunta['opciones']:
        v = IntVar()
        c1=Checkbutton(pregunta_lf,variable = v, bg='#DADADA',text = o, wraplength= 520, justify= LEFT, width = 75, height = 5, anchor = W, relief = GROOVE)
        c1.grid(row=r,column=0,pady=(0,10))
        r += 1
        opciones_widget.append(v)
    
    return opciones_widget


def opcion_unica(root,pregunta,pi):
    
    global r
    
    pregunta_lf = LabelFrame(root,bg = '#DADADA',text = 'Pregunta {}:'.format(pi),font=("Arial 12 bold"))
    pregunta_lf.grid(row=r,column=0,padx=(10,10),pady=(10,10))
    
    enunciado = Label(pregunta_lf,bg='#DADADA',text = pregunta['enunciado'],font=("Arial 9 bold"), wraplength= 600, justify= LEFT, width = 84, height = 6, anchor = W)
    enunciado.grid(row=r,column=0,padx=(10,10))
    
    r += 1
    opciones_widget = []
    v = IntVar()
    oi = 1
    for o in pregunta['opciones']:
        c1=Radiobutton(pregunta_lf,variable = v,value=oi, bg='#DADADA',text = o, wraplength= 520, justify= LEFT, width = 75, height = 5, anchor = W, relief = GROOVE)
        c1.grid(row=r,column=0,pady=(0,10))
        r += 1
        oi += 1
        opciones_widget.append((c1,v))

    return v

    
def realizar_test(nombre_test, test):
    
    global root
    global nombre_label
    global canvas
    global r
    global tipos
    global widgets
    global nombre
    global preguntas
    
    nombre = nombre_test
    preguntas = test
    
    root = Tk()
    
    root.title('Realizar Test')
    root.resizable(False, False)
    root.geometry('700x640')
    
    
    Label(root, text = nombre_test, font=("Arial 25 bold")).place(x=20,y=10)
    
    Label(root, text = 'Nombre:').place(x=20,y=60)    
    nombre_label = Entry(root)
    nombre_label.place(x=120,y=60)
    
    frame_root = Frame(root, bd=2,relief=SUNKEN)
    frame_root.grid_rowconfigure(0, weight=1)
    frame_root.grid_columnconfigure(0, weight=1)
    frame_root.place(x=20,y=100)
    
    yscrollbar = Scrollbar(frame_root)
    
    canvas = Canvas(frame_root, bd=0, width=640, height=450)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    
    frame_scrollable = Frame(canvas,bg='#B5B5B5')
    frame_scrollable.grid(row=0,column=0)
    
    canvas.create_window(0, 0, window=frame_scrollable,anchor='nw')
    
    yscrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=yscrollbar.set)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    
    frame_scrollable.bind("<Configure>", update_scrollregion)
    
    r = 0
    
    widgets = []
    
    test_resuelto = gx.leer_test_xml('tests_resueltos/'+nombre_test+'_resuelto',resultados=True)
    tipos = [comprobar_tipo_opcion(i['opciones']) for i in test_resuelto]
    
    for i in range(len(test)):
        if tipos[i] == 'multiple':
            widgets.append(opcion_multiple(frame_scrollable, test[i],i+1))
        else:
            widgets.append(opcion_unica(frame_scrollable, test[i],i+1))
                
    Button(root, text="Aceptar", command = aceptar, width=6).place(x=633,y=580)
    
    root.mainloop()


if __name__ == '__main__':
    #preguntas = [{'valoracion': 1, 'enunciado': 'También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.','tipo':'penalizado', 'opciones': [('o1_1 También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.', 1), ('o1_2', 451), ('o1_3', 451), ('o1_4', 451), ('o1_5', 451)]},{'valoracion': 2, 'enunciado': 'enunciado 2','tipo':'no-penalizado', 'opciones': [('o2_1', 824), ('o2_2', 498)]}]
    #preguntas = [{'valoracion': 1, 'enunciado': 'También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.','tipo':'penalizado', 'opciones': ['o1_1 También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.', 'o1_2', 'o1_3', 'o1_4', 'o1_5']},{'valoracion': 2, 'enunciado': 'enunciado 2','tipo':'no-penalizado', 'opciones': ['o2_1','o2_2']}]
    #print(preguntas)
    #realizar_test('Mi test', preguntas)    
    test = gx.leer_test_xml('tests/prueba')
    realizar_test('prueba',test)