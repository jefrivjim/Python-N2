import requests

def get_characters_page (page):
#def para obtener una pagina de los personajes
#recibe una pagina con numeros del 1-11 (paginas disponibles)
#devuelve el numero de id y nombre del personaje 
    response = requests.get (f"https://api.attackontitanapi.com/characters?page={page}")
    characters = response.json () ["results"]
    for x in characters:
        print (x ["id"],"-",x["name"])

def get_character_id (id):
#def para obtener un personaje especifico
#recibe el numero de id del personaje
#devuelve un diccionario del personaje accedido
    response = requests.get (f"https://api.attackontitanapi.com/characters/{id}")
    character = response.json ()
    return character

def get_titans ():
#def para obtener todos los titanes
#devuelve el id y nombre de cada titan
    response = requests.get ("https://api.attackontitanapi.com/titans")
    titan = response.json () ["results"]
    for x in titan:
        print (x["id"],"-",x["name"])

def get_titan_id (id):
#def para obtener un titan en especifico
#recibe el id de el titan del 1-9 (disponibles)
#devuelve un diccionario del titan accedido
    response = requests.get (f"https://api.attackontitanapi.com/titans/{id}")
    titan = response.json ()
    return titan


    


