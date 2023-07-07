import math

class Trig ():
    
    def __init__(self): #atributo que almacena el valor de Pi
        self.valorPi = math.pi
    
    def seno (self): #metodo para obtener seno de Pi
        seno = math.sin (self.valorPi)
        return seno

    def coseno (self): #metodo para obtener coseno de Pi
        coseno = math.cos (self.valorPi)
        return coseno

    def tangente (self): #metodo para obtener tangente de Pi
        tangente = math.tan (self.valorPi)
        return tangente
    



