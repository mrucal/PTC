# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:43:32 2017

@author: Mario
"""


from tkinter import *
from tkinter.simpledialog import *
from tkinter import StringVar


entrada = None
textVariable = None


def calcular_cuadrado():
    
    global entrada
    global textVariable
    
    root = Tk()
    
    root.geometry('300x100')
    root.title('Cuadrado')
    
    etiqueta = Label(root, text = 'El cuadrado de ')
    etiqueta.grid(row=0,column=0)
   
    entrada = Entry(root)
    entrada.grid(row=0,column=1)
    entrada.bind('<Return>',escribir_cuadrado)
    
    etiqueta2 = Label(root, text = ' es: ')
    etiqueta2.grid(row=0,column=2)

    textVariable = tkinter.StringVar(value='')
    resultado = Label(root, textvariable = textVariable)
    resultado.grid(row=0, column=3)

    root. mainloop()


def escribir_cuadrado(event):
    
    global entrada
    n = int(entrada.get())
    textVariable.set(n*n)
    
if __name__ == '__main__':
    
    print('ejecutando...')
    calcular_cuadrado()