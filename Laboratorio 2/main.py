from api import *
from ids import ids
import time
import asyncio
import aiohttp
import multiprocessing
import concurrent.futures
import threading

thread_local = threading.local ()


def getAllUsers (ids):
    with multiprocessing.Pool () as pool:
        diccionarios = pool.map (getOneUser, ids)
        return diccionarios
                
#Sin concurrencia (duracion aproximada 41 segundos)

if __name__== "__main__":
    start_time = time.time ()
    diccionario = getAllUsers(ids)
    for user in diccionario:
        print (user.get ("name"))
    duration = time.time () - start_time
    print (f"La duracion fue: {duration}")  













    
















 





    

    
