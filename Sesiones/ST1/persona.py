# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:57:27 2017

@author: Mario
"""


class Persona:
    
    def __init__(self, nombre, apellido, nacimiento, fallecimiento = (-1,-1,-1), domicilio=''):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.fallecimiento = fallecimiento
        self.domicilio = domicilio
        
    def esta_viva(self):
        return self.fallecimiento == (-1,-1,-1)
    
    def get_nombre(self):
        return self.nombre
    
    def get_apelldio(self):
        return self.apellido
            
    def get_nacimiento(self):
        return self.nacimiento
    
    def get_fallecimiento(self):
        return self.fallecimiento
    
    def get_domicilio(self):
        return self.domicilio
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apelldio(self, apellido):
        self.apellido = apellido
            
    def set_nacimiento(self, nacimiento):
        self.nacimiento = nacimiento
    
    def set_fallecimiento(self, fallecimiento):
        self.fallecimiento = fallecimiento
    
    def set_domicilio(self, domicilio):
        self.domicilio = domicilio
        
    def __repr__(self):
        s = '\n' + self.nombre+' '+self.apellido+' \nNacimiento: '+str(self.nacimiento[0])+'/'+str(self.nacimiento[1])+'/'+str(self.nacimiento[2])
        if not self.esta_viva():
            s +='\nFallecimiento: '+str(self.fallecimiento[0])+'/'+str(self.fallecimiento[1])+'/'+str(self.fallecimiento[2])
        if self.domicilio != '':
            s += '\nDireccion: '+self.domicilio
        s+= '\n'
        return s
    
if __name__ == '__main__':
        p = Persona('Mario', 'Ruiz', (28,12,1991))
        
        print(p)
        
        p.set_domicilio('Calle Horno')
        
        print(p,p.esta_viva())