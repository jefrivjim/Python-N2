import pandas as pd
import matplotlib.pyplot as plt
import get_characters as get_characters

import requests


titans = get_characters.get_titans ()

#ciclo for que cambia el valor "height" de la api por un valor int para poder crear el grafico
for titan in titans:
    new_height = int(titan["height"].replace ("m", "").replace ("~", "")) 
    titan["height"] = new_height





""" plt.bar (x,y, color=("lightblue"), edgecolor=["blue"])
plt.xlabel ("Titans")
plt.ylabel ("Height/Meters")
plt.title ("Titans height comparison")
plt.show () """



eldia_titans = 0
marley_titans = 0
neutral = 0

#ciclo for que aumenta 3 contadores, para identificar a que alianza pertenecen los titanes, de los contadores se generara un grafico
for x in titans:
    if x["allegiance"] == "Eldia":
        eldia_titans =+ eldia_titans+1
    elif x["allegiance"] == "Marley":
        marley_titans =+ marley_titans+1
    else:
        neutral=+neutral+1

""" menu = int(input ("Choose option 1 or option 2: "))

if menu == 1:
    df = pd.DataFrame (titans)
    x = df ["name"]
    y = df ["height"]
    fig, ax = plt.subplots()
    bar_height = ax.bar (x,y)
    ax.set (ylabel="Height/Meters", title= "Titans Height Comparison")
    ax.bar_label(bar_height, fmt='{:,.0f}')
    ax.bar (x,y, color="lightblue", edgecolor="blue")
    plt.show ()
elif menu == 2:
    labels = "Eldia", "Marley", "Neutral"
    sizes = eldia_titans, marley_titans, neutral

    fig, ax2= plt.subplots ()
    ax2.set (title= "Percentage of Titans owned by each side")
    ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
    plt.show()
else:
    print ("Choose a correct option")
 """
urls = ["https://api.attackontitanapi.com/characters?page=0","https://api.attackontitanapi.com/characters?page=1","https://api.attackontitanapi.com/characters?page=2","https://api.attackontitanapi.com/characters?page=3","https://api.attackontitanapi.com/characters?page=4","https://api.attackontitanapi.com/characters?page=5","https://api.attackontitanapi.com/characters?page=6","https://api.attackontitanapi.com/characters?page=7","https://api.attackontitanapi.com/characters?page=8","https://api.attackontitanapi.com/characters?page=9","https://api.attackontitanapi.com/characters?page=10","https://api.attackontitanapi.com/characters?page=11"]
characters = []

for url in urls:
    response = requests.get (url)
    character = response.json ()
    characters.append (character)

""" for x in characters:
    for y in x.keys ():
        if y == "results":
            for i in x["results"]:
                print (i["name"],i["status"]) """
            
            
response2= requests.get ("https://api.attackontitanapi.com/characters")
test = response2.json ()
print (test)