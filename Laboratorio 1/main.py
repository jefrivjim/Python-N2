from Clase_Trig import *
import os
from time import sleep
import datetime

menu = """Ingrese la opcion que desee
1- Seno
2- Coseno
3- Tangente
4- Salir
"""
opcion_elegida = int (input (menu))

#variable que crea el file
file = open ("log.txt", "a") 

#variable que llama la clase
valor = Trig ()

#bucle creado para seguir corriendo opciones hasta que el cliente seleccion opcion 4 == salir
while opcion_elegida != 4:
    if opcion_elegida == 1:
        resultado_seno = valor.seno ()
        print("el seno de pi es: ",resultado_seno)   
        file.write (f"\n{datetime.datetime.now ()}, operacion:seno, resultado:{resultado_seno}")
    elif opcion_elegida == 2:
        resultado_coseno = valor.coseno ()
        print("el coseno de pi es: ", resultado_coseno)
        file.write (f"\n{datetime.datetime.now ()}, operacion:coseno, resultado:{resultado_coseno}")
    elif opcion_elegida == 3:
        resultado_tangente = valor.tangente ()
        print("la tangente de pi es: ", resultado_tangente)
        file.write (f"\n{datetime.datetime.now ()}, operacion:tangente, resultado:{resultado_tangente}")
    else:
        print ("Ingrese una opcion correcta")
    
#espera 3 segundos antes de limpiar la pantalla para observar la respuesta
    sleep (3)

#limpia la pantalla despues de cada opcion elegida 
    os.system ("cls")
    opcion_elegida = int (input (menu))

#cierra el file al finalizar el bucle
file.close () 







    




    


