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
#devuelve una lista de todos los titanes
    response = requests.get ("https://api.attackontitanapi.com/titans")
    titan = response.json () ["results"]
    return titan

def get_titan_id (id):
#def para obtener un titan en especifico
#recibe el id de el titan del 1-9 (disponibles)
#devuelve un diccionario del titan accedido
    response = requests.get (f"https://api.attackontitanapi.com/titans/{id}")
    titan = response.json ()
    return titan

def get_all_characters_info ():
#def para obtener la informacion de todos los personajes
#devuelve una lista de diccionarios de todos los personajes
    urls = ["https://api.attackontitanapi.com/characters?page=0","https://api.attackontitanapi.com/characters?page=1","https://api.attackontitanapi.com/characters?page=2","https://api.attackontitanapi.com/characters?page=3","https://api.attackontitanapi.com/characters?page=4","https://api.attackontitanapi.com/characters?page=5","https://api.attackontitanapi.com/characters?page=6","https://api.attackontitanapi.com/characters?page=7","https://api.attackontitanapi.com/characters?page=8","https://api.attackontitanapi.com/characters?page=9","https://api.attackontitanapi.com/characters?page=10","https://api.attackontitanapi.com/characters?page=11"]
    characters = []

    for url in urls:
        response = requests.get (url)
        character = response.json ()
        characters.append (character)
    
    return characters



    


