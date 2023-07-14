from api import *
from ids import ids
import time
import multiprocessing
import concurrent.futures
import threading

#************* Sin concurrencia **********

""" def getAllUsers (ids):
    for id in ids: #iteracion entre la lista de ids
        user = getOneUser(id).get ("name") #variable que guarda el value de "name" de cada diccionario
        print (user)

if __name__=="__main__":
    start_time = time.time ()
    getAllUsers (ids) #llamado de funcion
    duration = time.time () - start_time
    print (f"La duracion fue de :{duration}") """


#***********Concurrencia usada (multiprocessing) *******************

def getAllUsers (ids):
    with multiprocessing.Pool () as pool:
            diccionarios = pool.map (getOneUser, ids) #genera una lista que corre en procesos diferentes
            return diccionarios #regresa la lista de diccionarios
                
if __name__== "__main__":
    start_time = time.time ()
    users = getAllUsers(ids)
    for user in users: #iteracion de la lista
        print (user.get ("name")) #imprime el value de "name" de cada diccionario
    duration = time.time () - start_time
    print (f"La duracion fue: {duration}")

#***********Concurrencia usada (threading)*********************

""" def getAllUsers (ids):
    with concurrent.futures.ThreadPoolExecutor (max_workers=5) as executor: #genera el pool de threads que corren concurrentemente
            users = list (executor.map (getOneUser, ids)) 
            return users #regresa la lista de diccionarios

if __name__=="__main__":
    start_time = time.time ()
    users = getAllUsers (ids)
    for user in users: #iteracion de cada diccionario
        print (user.get ("name")) #imprime el value de "name" de cada diccionario
    duration = time.time () - start_time
    print (f"La duracion fue de: {duration}") """












    
















 





    

    
