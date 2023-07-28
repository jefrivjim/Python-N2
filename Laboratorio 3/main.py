import get_chistes as get_chistes
import os
from time import sleep

menu = """
Selecciones una de las siguientes opciones para otener chistes de Chuck Norris 
1-Chiste random
2-Categorias de chistes
3-Salir 

"""

opcion_elegida = int (input(menu))

while opcion_elegida!=3:
    if opcion_elegida == 1:
        os.system ("cls")
        get_chistes.getRandomJoke () #llamada funcion 
        print ()
    elif opcion_elegida==2:
        os.system ("cls")
        count = 1
        for category in get_chistes.getCategoriesList(): #recorre la lista obtenida y usa variable count para agregar un numero a cada objeto
            print (str(count),"-",category.capitalize())
            count += 1
        length = len (get_chistes.getCategoriesList()) 

        menu_categories = input (f"Ingrese una opcion del 1 al {length}\n")
        menu_categories = int (menu_categories) -1
        opcion_elegida = get_chistes.getCategoriesList ()[menu_categories] #elige la opcion basado en el numero ingresado
        print ("La opcion elegida fue ",opcion_elegida)
        get_chistes.getCategoryJoke (opcion_elegida) #llamada funcion
                            
    else:
        os.system ("cls")
        print ("Seleccione una opcion correcta")
    
    opcion_elegida = int (input(menu))

print ("Usted eligio salir")
print ("CHUCK NORRIS DOESN'T APPROVE THIS")
