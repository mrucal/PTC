# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:06:38 2017

@author: Mario
"""

import random
from tkinter import *
from tkinter.simpledialog import *

entrada = None
textVariable = None
goal = None
root = None

def aleatorio():
    
    global entrada
    global textVariable
    global goal
    global root
    
    goal = random.randint(1,100)
    
    root = Tk()
    
    root.geometry('200x100')
    root.title('Aleatorio')
    
    entrada = Entry(root)
    entrada.grid(row=0,column=1)
    entrada.bind('<Return>',recibir_numero)
    
    textVariable = tkinter.StringVar(value='')
    resultado = Label(root, textvariable = textVariable)
    resultado.grid(row=1, column=1)
    
    root. mainloop()
    
def recibir_numero(event):
    
    global entrada
    global goal
    global root
    
    n = int(entrada.get())
    
    print(goal)
    
    if n == goal:
        textVariable.set('Has acertado el numero!!')
        salir = Button(root,text='Salir')
        salir.grid(row=3,column=1)
    else:
        if n < goal:
            textVariable.set(str(n)+' es menor')
        else:
            textVariable.set(str(n)+' es mayor')
    
if __name__ == '__main__':
    
    print('ejecutando...')
    aleatorio()