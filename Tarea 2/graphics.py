import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_titans ():
#def para obtener todos los titanes
#devuelve el id y nombre de cada titan
    response = requests.get ("https://api.attackontitanapi.com/titans")
    titan = response.json () ["results"]
    return titan

titans = get_titans ()

for titan in titans:
    new_height = int(titan["height"].replace ("m", "").replace ("~", ""))
    titan["height"] = new_height


df = pd.DataFrame (titans)
x = df ["name"]
y = df ["height"]


""" plt.bar (x,y, color=("lightblue"), edgecolor=["blue"])
plt.xlabel ("Titans")
plt.ylabel ("Height/Meters")
plt.title ("Titans height comparison")
plt.show () """

fig, ax = plt.subplots()
bar_height = ax.bar (x,y)
ax.set (ylabel="Height/Meters", title= "Titans Height Comparison")
ax.bar_label(bar_height, fmt='{:,.0f}')
ax.bar (x,y, color="lightblue", edgecolor="blue")
plt.show ()