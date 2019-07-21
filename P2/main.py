# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 04:36:52 2018

@author: Mario
"""


from tkinter import *


import crear_test as ct
import abrir_test as at


def crear():
    global root
    root.destroy()
    ct.crear_test()
   
    
def realizar():
    global root
    root.destroy()
    at.abrir_test()


def corregir():
    global root
    root.destroy()
    at.abrir_test(corregir=True)


def main():
    
    global root
    
    root = Tk()
    
    root.title('Práctica 2')
    root.resizable(False, False)
    root.geometry('500x370')
    
    root.configure(background='#DADADA')
    
    Button(root, text="Crear Test", bg='#6699FF', font=("Arial 12 bold"), command = crear, width=39,height=3).place(x=50,y=50)
    Button(root, text="Realizar Test", bg='#ADFF5B', font=("Arial 12 bold"), command = realizar, width=39,height=3).place(x=50,y=150)
    Button(root, text="Corregir Test", bg='#FFFF99', font=("Arial 12 bold"), command = corregir, width=39,height=3).place(x=50,y=250)
    
    root.mainloop()

    

if __name__ == '__main__':
    main()
    