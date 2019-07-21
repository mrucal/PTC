# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:43:32 2017

@author: Mario
"""


from tkinter import *
from tkinter.simpledialog import *
import math

entrada = None
entrada_funcion = None
textVariable = None


def calcular_funcion():
    
    global entrada
    global entrada_funcion
    global textVariable
    
    root = Tk()
    
    root.geometry('400x100')
    root.title('Funcion')
    
    entrada_funcion = Entry(root)
    entrada_funcion.grid(row=0,column=0)
    
    etiqueta = Label(root, text = ' de ')
    etiqueta.grid(row=0,column=1)
   
    entrada = Entry(root)
    entrada.grid(row=0,column=2)
    entrada.bind('<Return>',escribir_funcion)
    
    etiqueta2 = Label(root, text = ' es: ')
    etiqueta2.grid(row=0,column=3)

    textVariable = tkinter.StringVar(value='')
    resultado = Label(root, textvariable = textVariable)
    resultado.grid(row=0, column=4)

    root. mainloop()


def escribir_funcion(event):
    
    global entrada
    f = entrada_funcion.get()
    n = entrada.get()
    exp = 'math.'+f+'('+n+')'
    textVariable.set(eval(exp))
    
if __name__ == '__main__':
    
    print('ejecutando...')
    calcular_funcion()