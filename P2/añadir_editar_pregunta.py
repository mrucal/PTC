# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:39:47 2017

@author: Mario
"""


from tkinter import *
from tkinter.messagebox import *


b_añadir_opcion = None
b_eliminar_opcion = None
b_aceptar = None
opciones_lf = None
n = 2
opciones_val = []
root = None
y_root = 365

valoracion_val = None
enunciado_val = None

pregunta = {}


def comprobar_puntuaciones(puntuaciones):
    
    error = False
    positivas = [i for i in puntuaciones if i>0]
    negativas = [i for i in puntuaciones if i<0]
    
    cp = 0
    
    for i in positivas:
        cp += i
    
    if cp != 100 or len(positivas) == len(puntuaciones):
        showinfo(title='ERROR',message='Revisar puntuaciones.')
        error = True
    
    if len(negativas)>0:
        if len(positivas) + len(negativas) != len(puntuaciones):
            showinfo(title='ERROR',message='Revisar puntuaciones. No puede haber puntuaciones negativas y vacías.')
            error = True
        else:
            cn = 0
            for i in negativas:
                cn += -i 
            if cn != int(100-round(100/len(puntuaciones),0)):
                showinfo(title='ERROR',message='Revisar puntuaciones. Las puntuaciones negativas deben sumar -{}.'.format(int(100-round(100/len(puntuaciones),0))))
                error = True

    return error
        

def aceptar():
    
    global valoracion_val
    global enunciado_val
    global root
    global opciones_val
    global pregunta
    
    pregunta = {}
    error = False
    
    try:
        if valoracion_val.get() != '':
            pregunta['valoracion']=(int(valoracion_val.get()))
        else:
            # Si el campo valoración se deja vacío, por defecto será 1
            pregunta['valoracion'] = 1
    except:
        showinfo(title='ERROR',message='El campo valoración debe ser entero.')
        error = True
    
    # Obtener campo enunciado
    pregunta['enunciado'] = enunciado_val.get(0.0, END)[:-1]

    if pregunta['enunciado'] == '':
        showinfo(title='ERROR',message='El campo enunciado no puede estar vacio.')
        error = True
    
    pregunta['opciones'] = []
    n=0
    puntuaciones = []
    for i in opciones_val:
        n+=1
        opcion_txt = i[1].get(0.0,END)
        if opcion_txt == '\n':
            showinfo(title='ERROR',message='El campo texto de la opción O{} no puede estar vacio.'.format(n))
            error = True
            
        opcion_val = i[2].get(0.0,END)
        if opcion_val != '\n':
            try:
                opcion_val = int(opcion_val)
            except:
                showinfo(title='ERROR',message='El campo puntuación de la opción O{} debe ser entero.'.format(n))
                error = True
        else:
            opcion_val = 0
        
        puntuaciones += [opcion_val]
        pregunta['opciones'].append((opcion_txt[:-1],opcion_val))
    
    # Comprobar que las puntuaciones de cada opción cumplen las normas
    error = comprobar_puntuaciones(puntuaciones)
        
    if not error:
        root.destroy()
    else:
        pregunta = {}    
    

def añadir_opcion():
    
    global b_añadir_opcion
    global b_eliminar_opcion
    global b_aceptar
    global opciones_lf
    global n
    global opciones_val
    global root
    global y_root
    
    # Solo se permiten 8 opciones como máximo
    if n<8:
        n+=1
        
        # Añadir la opción
        on = Label(opciones_lf, bg='#DADADA',text = 'O'+str(n))
        on.grid(row=n,column=0,pady=(10,10))
        on_txt = Text(opciones_lf, width=30, height = 2)
        on_txt.grid(row=n,column=1,pady=(10,10))
        
        on_val = Text(opciones_lf, width=5, height = 1)
        on_val.grid(row=n,column=2,pady=(10,10))
        
        op=Label(opciones_lf, bg='#DADADA',text = '%')
        op.grid(row=n,column=3)
        
        opciones_val.append((on,on_txt,on_val,op))
        
        # Posicionar la opción, teniendo en cuenta la posición de la última
        y_root+=55
        root.geometry('470x'+str(y_root))
        
        # Volver a posicionar los botones
        b_añadir_opcion.grid(row=n+1,column=2,pady=(10,10))
        b_eliminar_opcion.grid(row=n+1,column=0,pady=(10,10))
        b_aceptar.place(x=398,y=y_root-30)
    
    
def eliminar_opcion():
    
    global b_añadir_opcion
    global b_eliminar_opcion
    global b_aceptar
    global n 
    global y_root
    
    # Debe haber como mínimo 2 opciones
    if n>2:
        n-=1
        
        # Destruir los widgets asociados a la última opción
        for i in opciones_val[-1]:
            i.destroy()
        
        del opciones_val[-1]
        
        # Actualizar la posición de la última opción
        y_root-=55
        root.geometry('470x'+str(y_root))
        
        # Volver a posicionar los botones
        b_añadir_opcion.grid(row=n+1,column=2,pady=(10,10))
        b_eliminar_opcion.grid(row=n+1,column=0,pady=(10,10))
        b_aceptar.place(x=398,y=y_root-30)
    

def añadir_editar_pregunta(root_local=None, editar_pregunta = ""):
    
    global b_añadir_opcion
    global b_eliminar_opcion
    global b_aceptar
    global opciones_lf
    global opciones_val
    global root
    global y_root
    global ultima_opcion
    global pregunta
    global valoracion_val
    global enunciado_val
    
    opciones_val = []
    
    if editar_pregunta != '':
        pregunta = editar_pregunta
    else:
        pregunta = {}
    
    if root_local == None:
        root = Tk()
    else:
        root = root_local
    
    root.title('Nueva Pregunta')
    root.resizable(False, False)
    root.geometry('470x'+str(y_root))
    
    
    Label(root, text = 'Valoración:').place(x=20,y=10)    
    valoracion_val = Entry(root)
    valoracion_val.place(x=100,y=10)
    # Si se esta editando la pregunta, mostrar el campo antiguo
    if editar_pregunta != '':
        valoracion_val.insert(INSERT, editar_pregunta['valoracion'])
    
    
    Label(root, text = 'Enunciado:').place(x=20,y=35)
    enunciado_val = Text(root, width=43, height = 5)
    enunciado_val.place(x=100,y=35)
    # Si se esta editando la pregunta, mostrar el campo antiguo
    if editar_pregunta != '':
        enunciado_val.insert(INSERT, editar_pregunta['enunciado'])
    
    
    opciones_lf = LabelFrame(root,bg = '#DADADA', text = 'Opciones:')
    opciones_lf.place(x=20,y=125)
    Label(opciones_lf, bg='#DADADA',text = '           Número      ').grid(row=0,column=0)
    Label(opciones_lf, bg='#DADADA',text = 'Texto').grid(row=0,column=1)
    Label(opciones_lf, bg='#DADADA',text = 'Puntuación').grid(row=0,column=2)
          
    
    # Opción 1
    o1 = Label(opciones_lf, bg='#DADADA',text = 'O1')
    o1.grid(row=1,column=0,pady=(10,10))
    o1_txt = Text(opciones_lf, width=30, height = 2)
    o1_txt.grid(row=1,column=1,pady=(10,10))
    if editar_pregunta != '':
        o1_txt.insert(INSERT, editar_pregunta['opciones'][0][0])
    o1_val = Text(opciones_lf, width=5, height = 1)
    o1_val.grid(row=1,column=2,pady=(10,10))
    if editar_pregunta != '':
        o1_val.insert(INSERT, editar_pregunta['opciones'][0][1])
    op=Label(opciones_lf, bg='#DADADA',text = '%')
    op.grid(row=1,column=3)
    # Guardar los widgets para obtener los datos
    opciones_val.append((o1,o1_txt,o1_val,op))

    
    # Opción 2
    o2 = Label(opciones_lf, bg='#DADADA',text = 'O2')
    o2.grid(row=2,column=0,pady=(10,10))
    o2_txt = Text(opciones_lf, width=30, height = 2)
    o2_txt.grid(row=2,column=1,pady=(10,10))
    if editar_pregunta != '':
        o2_txt.insert(INSERT, editar_pregunta['opciones'][1][0])
    o2_val = Text(opciones_lf, width=5, height = 1)
    o2_val.grid(row=2,column=2,pady=(10,10))
    if editar_pregunta != '':
        o2_val.insert(INSERT, editar_pregunta['opciones'][1][1])
    op=Label(opciones_lf, bg='#DADADA',text = '%')
    op.grid(row=2,column=3)
    opciones_val.append((o2,o2_txt,o2_val))
    
    b_añadir_opcion = Button(opciones_lf, text="+", command = añadir_opcion, width=2)
    b_eliminar_opcion = Button(opciones_lf, text="-", command = eliminar_opcion, width=2)
    b_aceptar = Button(root, text="Aceptar", command = aceptar, width=6)
    
    
    # Si se está editando la pregunta y tiene más de dos opciones, mostrarlas
    if editar_pregunta != '' and len(editar_pregunta['opciones']) > 2:
        y_root = 365
        for i in range(2,len(editar_pregunta['opciones'])):
            n = i+1
            on = Label(opciones_lf, bg='#DADADA',text = 'O'+str(n))
            on.grid(row=n,column=0,pady=(10,10))
            on_txt = Text(opciones_lf, width=30, height = 2)
            on_txt.grid(row=n,column=1,pady=(10,10))
                
            on_txt.insert(INSERT, editar_pregunta['opciones'][i][0])
            on_val = Text(opciones_lf, width=5, height = 1)
            on_val.grid(row=n,column=2,pady=(10,10))

            on_val.insert(INSERT, editar_pregunta['opciones'][i][1])
            
            op=Label(opciones_lf, bg='#DADADA',text = '%')
            op.grid(row=n,column=3)
                
            opciones_val.append((on,on_txt,on_val))
                   
            y_root+=55
            root.geometry('470x'+str(y_root))
            
            b_añadir_opcion.grid(row=n+1,column=2,pady=(10,10))
            b_eliminar_opcion.grid(row=n+1,column=0,pady=(10,10))
            b_aceptar.place(x=398,y=y_root-30)            
    
    else:
        b_añadir_opcion.grid(row=3,column=2,pady=(10,10))
        b_eliminar_opcion.grid(row=3,column=0,pady=(10,10))
        b_aceptar.place(x=398,y=y_root-30)


if __name__ == '__main__':
    
    print('ejecutando...')
    añadir_editar_pregunta()    