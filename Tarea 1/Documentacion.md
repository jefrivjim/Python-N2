# API utilizada Atackontitanapi

Endpoints utilizados
1. https://api.attackontitanapi.com/characters (despliega lista de personajes, divididos en 11 paginas)
2. https://api.attackontitanapi.com/characters/188 (despliega un personaje en especifico)
3. https://api.attackontitanapi.com/titans (despliega todos los titanes)
4. https://api.attackontitanapi.com/titans/1 (despliega un titan en especifico)

Se crearon 4 funciones, guardados en archivo **get_characters.py**

1. **get_characters_page**
- def para obtener una pagina de los personajes
- recibe una pagina con numeros del 1-11 (paginas disponibles)
- devuelve el numero de id y nombre del personaje

2. **get_character_id** 
- def para obtener un personaje especifico
- recibe el numero de id del personaje
- devuelve un diccionario del personaje accedido

3. **def get_titans**
- def para obtener todos los titanes
- devuelve el id y nombre de cada titan

4. **def get_titan_id**
- def para obtener un titan en especifico
- recibe el id de el titan del 1-9 (disponibles)
- devuelve un diccionario del titan accedido

Finalmente se corren desde el archivo **main.py**