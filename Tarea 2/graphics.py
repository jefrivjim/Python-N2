import pandas as pd
import matplotlib.pyplot as plt
import get_characters as get
import os 
import time

menu = """
SHINGEKI NO KYOJIN DATABASE
Interesting Information

Choose one of the following options to get more information and comparisons:

1- Titans History
2- Graphics and Comparisons
3- Exit 

Option selected: """

graphics_menu = """Choose the graphic you want to see: 
1- Titans height comparison
2- Percentage of titans owned by Eldia and Marley
3- Percentage of characters reported as alive or dead
Option: """

#ciclo for que cambia el valor "height" de la api por un valor int para poder crear el grafico
titans = get.get_titans ()
for titan in titans:
    new_height = int(titan["height"].replace ("m", "").replace ("~", "")) 
    titan["height"] = new_height

#ciclo for que aumenta 3 contadores, para identificar a que alianza pertenecen los titanes, de los contadores se generara un grafico
eldia_titans = 0
marley_titans = 0
neutral = 0
for x in titans:
    if x["allegiance"] == "Eldia":
        eldia_titans =+ eldia_titans+1
    elif x["allegiance"] == "Marley":
        marley_titans =+ marley_titans+1
    else:
        neutral=+neutral+1

#ciclo for que aumenta 3 contadores, para identificar cuantos personajes se reportan como muertos o vivos, se genera un grafico que compara los valores
dead = 0
alive = 0
unknown = 0

for x in get.get_all_characters_info ():
    for y in x.keys ():
        if y == "results":
            for i in x["results"]:
                if i["status"] == "Deceased":
                    dead =+ dead+1
                elif i["status"] == "Alive":
                    alive =+ alive+1
                else:
                    unknown =+ unknown+1

option = int(input(menu))
titans_menu = True

while option != 3:
    if option == 1:
        os.system ("cls")
        print ("""AFTER HER DEATH, YMIR's SOUL WAS SPLIT INTO NINE TITANS, 
WHO BUILT THE EMPIRE OF ELDIA.""")
        time.sleep (5)
        os.system ("cls")
        print ("""The Nine Titans were nine Titan
powers that had been passed down through
the Eldian people for nearly 2,000 years 
after the death of Ymir Fritz until the death
of Eren Yeager, with each having their own name. 
The nine Titan powers were the Founding Titan, 
the Armored Titan, the Attack Titan, 
the Beast Titan, the Cart Titan, the Colossus Titan, 
the Female Titan, the Jaw Titan and the War Hammer Titan.\n""")
        back_menu = input ("Press Enter to go back to the main menu: ")
        while back_menu != "":
            back_menu = input ("Press Enter to go back to the main menu: ")
    elif option == 2:
        os.system("cls")
        graphics = int (input(graphics_menu))
        while titans_menu:
            if graphics == 1:
                df = pd.DataFrame (titans)
                x = df ["name"]
                y = df ["height"]
                fig, ax = plt.subplots()
                bar_height = ax.bar (x,y)
                ax.set (ylabel="Height/Meters", title= "Titans Height Comparison")
                ax.bar_label(bar_height, fmt='{:,.0f}')
                ax.bar (x,y, color="lightblue", edgecolor="blue")
                plt.show ()
                titans_menu = False
            elif graphics == 2:
                labels = "Eldia", "Marley", "Neutral"
                sizes = eldia_titans, marley_titans, neutral
                fig, ax2= plt.subplots ()
                ax2.set (title= "Percentage of Titans owned by each side")
                ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
                plt.show()
                titans_menu = False
            elif graphics == 3:
                labels2 = "Dead", "Alive", "Unknown"
                sizes2 = dead, alive, unknown
                fig, ax2= plt.subplots ()
                ax2.set (title= "Percentage of all characters reported as dead or alive")
                ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', shadow=True)
                plt.show()
                titans_menu = False
            else:
                print ("Enter a valid option")
                time.sleep (3)
                os.system ("cls")
                graphics = int (input(graphics_menu))
    else:
        print ("Enter valid option")
        time.sleep (2)         

    os.system ("cls")
    option = int(input(menu))
    titans_menu = True
