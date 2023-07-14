from api import *
from ids import ids
import time


start_time = time.time ()

for id in ids:
    diccionarios = dict(getOneUser (id))
    print (diccionarios.get ("name"))

duration = time.time () - start_time

print (f"La duracion fue: {duration}")


    

    
