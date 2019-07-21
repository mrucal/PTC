# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:11:16 2018

@author: Mario
"""

from tkinter import *
from tkinter.messagebox import *
import json
import os
import matplotlib.pyplot as plt
from PIL import Image
import gestionar_xml as gx

def cerrar():
    global root
    root.destroy()


def calcular_calificacion(valoraciones,puntuaciones,tipos,respuestas):
    
    calificacion = 0
    calificacion_pregunta = []
    for i in range(len(valoraciones)):
        if tipos[i] != 'multiple':
            calificacion += valoraciones[i] * (puntuaciones[i][respuestas[i]]/100)
            calificacion_pregunta.append(valoraciones[i] * (puntuaciones[i][respuestas[i]]/100))
        else:
            calificacion_m = 0
            for m in respuestas[i]:
                calificacion += valoraciones[i] * (puntuaciones[i][m]/100)
                calificacion_m += valoraciones[i] * (puntuaciones[i][m]/100)
            calificacion_pregunta.append(calificacion_m)
                
    if calificacion < 0:
        calificacion = 0
    
    return [calificacion, calificacion_pregunta]


def guardar_calificacion(nombre_test,nombre_realizador, calificacion):
    
    try:
        with open('calificaciones/'+nombre_test+'.json', 'r',encoding='utf-8') as file:
            calificaciones_json = json.load(file)
    except:
        calificaciones_json = []
    
    realizadores = [i[0] for i in calificaciones_json]
    
    if nombre_realizador in realizadores:
        for r in calificaciones_json:
            if r[0] == nombre_realizador:
                r[1] = calificacion
    else:
        calificaciones_json.append((nombre_realizador,calificacion))
    
    try:
        os.stat('calificaciones/')
    except:
        os.mkdir('calificaciones/')   
    
    with open('calificaciones/'+nombre_test+'.json','w',encoding='utf-8') as file:
        json.dump(calificaciones_json,file)
        
        
def obtener_todas_calificaciones(nombre_test):
    
    try:
        with open('calificaciones/'+nombre_test+'.json', 'r',encoding='utf-8') as file:
            calificaciones_json = json.load(file)
    except:
        calificaciones_json = []

    calificaciones = [i[1][0] for i in calificaciones_json]
        
    return calificaciones
    

def dibuja(nombre_test,calificaciones):
    
    #calificaciones = [c[0] for c in calificaciones]
    calificaciones.sort()
    stats = [0]*10
    for i in calificaciones:
        stats[int(i-0.0001)] += 1
    impr = ['[0,1]'] + ['({},{}]'.format(i,i+1) for i in range(1,10)]
        
    plt.figure() 
    plt.pie([s for s in stats if s>0], labels=[impr[i] for i,s in enumerate(stats) if s>0], autopct='%1d%%', shadow=True)
    plt.savefig('calificaciones/'+nombre_test+'.png')
    
    im = Image.open('calificaciones/'+nombre_test+'.png')
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)
    im.save('calificaciones/'+nombre_test+'.gif', transparency=255)
    
    os.remove('calificaciones/'+nombre_test+'.png')
    
    plt.figure() 
    plt.ylim(0,max(stats)+1)
    plt.bar(range(10), stats)
    plt.xticks(range(10), impr)
    plt.savefig('calificaciones/'+nombre_test+'_histo.png')
    
    im = Image.open('calificaciones/'+nombre_test+'_histo.png')
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)
    im.save('calificaciones/'+nombre_test+'_histo.gif', transparency=255)
    
    os.remove('calificaciones/'+nombre_test+'_histo.png')
    
def update_scrollregion(event):
    global canvas
    canvas.configure(scrollregion=canvas.bbox("all"))
    
def corregir_test_i(nombre_test, nombre_realizador, valoraciones, puntuaciones, tipos, respuestas,frame_scrollable,i):
    
    calificacion = calcular_calificacion(valoraciones,puntuaciones,tipos,respuestas)

    guardar_calificacion(nombre_test,nombre_realizador, calificacion)
    
    calificacion_lf = LabelFrame(frame_scrollable,bg = '#DADADA',text = nombre_realizador,font=("Arial 16 bold"))
    calificacion_lf.grid(row=i,column=0,padx=(10,10),pady=(10,10))
    
    Label(calificacion_lf, text = 'Has obtenido un:\n'+str(calificacion[0]), font=("Arial 25 bold"),bg = '#DADADA',width=42, height=2).grid(row=0,column=0)
    for i,c in enumerate(calificacion[1]):
          Label(calificacion_lf, text = 'Pregunta '+str(i+1)+': '+str(c),bg = '#DADADA',width=42, height=1).grid(row=i+1,column=0)


def corregir_test(nombre_test, nombre_realizador, valoraciones, puntuaciones, tipos, respuestas):
    
    global root
    global canvas
    
    root = Tk()
    
    root.title('Calcular calificación')
    root.resizable(False, False)
    root.geometry('940x640')
    
    Label(root, text = nombre_test, font=("Arial 25 bold")).place(x=20,y=10)
    
    frame_root = Frame(root, bd=2,relief=SUNKEN)
    frame_root.grid_rowconfigure(0, weight=1)
    frame_root.grid_columnconfigure(0, weight=1)
    frame_root.place(x=20,y=60)
    
    yscrollbar = Scrollbar(frame_root)
    
    canvas = Canvas(frame_root, bd=0,width=868, height=210)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    
    frame_scrollable = Frame(canvas,bg='#B5B5B5')
    frame_scrollable.grid(row=0,column=0)
    
    canvas.create_window(0, 0, window=frame_scrollable,anchor='nw')
    
    yscrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=yscrollbar.set)
    yscrollbar.grid(row=0, column=1, sticky=N+S)
    
    frame_scrollable.bind("<Configure>", update_scrollregion)
    
    for i in range(len(valoraciones)):
        corregir_test_i(nombre_test, nombre_realizador[i], valoraciones[i], puntuaciones[i], tipos[i], respuestas[i],frame_scrollable,i)
        
    stats = obtener_todas_calificaciones(nombre_test)
    dibuja(nombre_test,stats)
    
    tkimage = PhotoImage(file="calificaciones/"+nombre_test+".gif")
    label = Label(image=tkimage)
    label.place(x=20,y=300)
    
    tkimage2 = PhotoImage(file="calificaciones/"+nombre_test+"_histo.gif")
    label2 = Label(image=tkimage2)
    label2.place(x=476,y=300)
    
    Button(root, text="Cerrar", command = cerrar, width=6).place(x=860,y=600)
    
    root.mainloop()
    

if __name__ == '__main__':
    print('ejecutando...')
    valoraciones = [[2.5, 2.5, 2.5, 2.5]]
    puntuaciones = [[[0, 100, 0, 0], [100, -50], [50, -25, -25, 50], [-33, 100, -34]] ]
    tipos = [['no-penalizado', 'no-penalizado', 'multiple', 'penalizado']]
    #respuestas = [1, 1, [1], 1]
    respuestas = [[1, 0, [0,3], 1]]
    corregir_test('prueba',['ales'],valoraciones,puntuaciones,tipos,respuestas)
    calificaciones = [5.1,10,8.4,2.6,1.2,0.5,9.4,7.4,5.1,7,1,0,2,1,9]
    #dibuja('prueba',calificaciones)
    