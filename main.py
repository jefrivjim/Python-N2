import get_characters as get_characters
import os
import time

menu = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⣿⠀⠀⠀⠀
⣀⣀⣀⣀⣀⣸⣿⣿⣷⣄⣀⣄⣄⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡴⠋⠀⣸⣧⣤⣤⣤⣤
⣿⠉⣉⣉⣉⣉⣹⣿⣿⣿⣿⣄⣀⣀⣀⣈⣉⣉⣉⣉⠉⢁⣁⣀⣀⣀⣉⣉⣉⣉⣉⡽⠋⠀⠀⣠⣟⣀⣀⣀⠀⣿
⣿⠀⡿⣿⣯⡉⠉⠙⣿⣿⣿⣿⣯⡉⠉⠉⠉⠉⠉⣿⠀⢸⡏⠉⠉⠉⠉⠉⢉⡽⠋⠀⠀⢀⣴⠋⣩⡿⢻⣿⠀⣿
⣿⠀⡇⠘⣿⣿⣷⣄⡈⠛⢿⣿⣿⡇⣶⣄⠀⠀⠀⣿⠀⢸⡇⠀⠀⠀⢀⡴⢻⡇⠀⢀⣴⢟⡵⠟⠁⢀⡾⢸⠀⣿
⣿⠀⡇⠀⠹⣿⣿⣿⣿⣶⣄⡙⢿⡇⣿⣿⣷⣄⠀⣿⠀⢸⡇⠀⢀⡴⠋⠀⢸⣇⣴⡿⠟⠉⠀⠀⢀⣼⠃⢸⡀⣿
⣿⠀⣷⣶⣦⣌⡛⢿⣿⣿⣿⣧⢰⣅⠻⣿⣿⣿⣷⣿⠀⢸⣇⠴⠋⠀⠀⣠⣾⠟⣿⠇⠀⢀⣠⣾⠿⠓⠋⢩⡇⣿
⣿⠀⡟⢿⣿⣿⣿⣶⣌⡻⢿⣿⣸⣿⣷⣌⠻⣿⣿⣿⣧⣾⡇⠀⢀⣴⣾⠟⠁⢰⣿⣠⣴⡿⠛⠁⠀⠀⣠⢿⠀⣿
⣿⠀⣇⠀⠙⠿⣿⣿⣿⣿⣇⢉⡙⢿⣿⣿⣧⠈⣹⠟⠁⣿⣇⣴⣿⠟⠁⠀⣠⣾⢿⣿⠉⠀⠀⣀⣴⣾⡧⣼⠀⣿
⣿⠀⣿⣿⣶⣦⣌⠛⠿⣿⣿⡜⣿⣦⡻⠋⣡⠎⠀⠀⢀⣿⣿⡏⠁⠀⣠⡾⠟⠁⣼⡇⣀⣴⣾⠿⠛⠁⢀⣿⡅⣿
⣿⠀⣿⣿⣿⣿⣿⣿⣦⡈⠙⠃⠹⣿⡿⢸⠃⠀⣠⣾⠿⢋⣿⠃⣠⡾⠋⠀⠀⣠⣿⣿⡿⠋⠀⠀⠀⢀⡞⢹⠂⣿
⣿⠀⠿⠿⠿⢿⣿⣿⣿⣷⡌⢿⣦⣽⣷⡏⢀⣴⠟⠁⠀⢸⣿⡿⠋⠀⠀⣠⡾⠟⢩⣿⠃⠀⠀⢀⡴⣛⣛⣿⡁⣿
⣿⠀⣰⣶⣦⣤⣙⣻⣿⣿⣷⡘⣿⣿⣿⣷⡿⠋⠀⢀⣴⢿⣿⠀⢀⣴⠾⠋⠀⢀⣿⡏⣠⣴⣾⡿⠟⠉⢀⣾⠀⣿
⣿⠀⡟⢻⣿⣿⣿⣿⣭⣉⠙⠃⠘⢿⣿⡏⠀⢀⣴⠟⠁⣸⣿⣾⡟⠁⠀⠀⣀⣼⣿⣿⡿⠛⠁⠀⠀⢠⡞⢹⠀⣿
⣿⠀⡇⠀⠙⢿⣿⣿⣿⣿⣆⢲⣤⣄⣹⢁⣴⠟⠁⢀⣴⠟⢻⣿⠀⢀⣤⣾⡿⠛⣹⡟⠀⠀⢀⣠⣴⣋⣀⢸⠀⣿
⣿⠀⣧⣴⣦⣤⣈⡙⠻⣿⣿⡌⣿⣿⣿⡿⠋⢀⣴⠟⠃⢀⣿⣷⣾⠿⠋⠁⠀⢠⣿⣣⣴⠾⠛⠋⠉⣹⠏⢸⡄⣿
⣿⠀⣿⠈⠻⣿⣿⣿⣷⣦⡈⠁⠘⠻⣿⠀⣠⡾⠃⢀⣴⣿⣿⡟⠁⠀⣀⣴⣾⣿⣿⠟⠁⠀⠀⢀⡼⠃⠀⢸⠆⣿
⣿⠀⣿⠀⠀⠈⠻⣿⣿⣿⣿⡌⢿⣷⣿⡾⠋⢀⣴⠟⠉⢸⣿⣠⣶⡿⠟⠛⠉⣼⡏⢀⣠⣤⣶⠿⠶⣶⠀⢸⡀⣿
⣿⠀⣿⠰⣿⣿⣶⣦⣌⡉⠛⠻⠈⢿⡏⢀⡴⠟⠁⣠⣴⣿⣿⡟⠉⠀⠀⣀⣸⣿⣾⠿⠛⠉⠀⣀⡾⠃⠀⢸⠀⣿
⣿⠀⣿⠀⠈⠛⢿⣿⣿⣿⣿⣦⢠⣼⡷⢋⣠⣶⡿⠟⠋⣽⣏⣀⣤⣶⣿⠿⢻⣿⠁⠀⣀⣤⠾⠋⠀⠀⠀⢸⡀⣿
⣿⠀⡇⠀⠀⠀⢠⣬⣉⡛⠿⢿⣧⣹⣶⡿⠛⠉⢀⣠⣴⣿⠿⠟⠋⠁⠀⣠⣿⣷⠶⠛⠛⢋⡿⠁⠀⠀⠀⢸⡇⣿
⣿⠀⢷⣄⡀⠀⠈⠻⣿⣿⣿⣶⣦⡟⠉⣀⣤⠶⠛⢉⣿⠇⣀⣠⡴⠶⠛⣽⡟⠀⠀⢀⣠⠟⠀⠀⠀⣀⣤⡾⠃⣿
⠻⢦⣄⡈⠛⠶⣤⣀⠈⠙⠛⠿⣿⡷⠟⠋⢀⣠⣴⣿⡿⠛⠉⠁⣀⣠⣾⣿⣴⡶⠿⢯⣤⣀⣤⡶⠟⠋⣁⣤⡶⠟
⠀⠀⠉⠻⢶⣤⣈⠙⠳⣿⣿⣷⣏⣤⣴⠾⠛⠉⣠⣿⣣⣴⡶⠿⣻⡿⠋⠉⠀⠀⢀⣴⠿⠛⢁⣠⡴⠞⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠷⣦⣄⣽⠿⠋⠉⠀⢀⣠⣾⣿⣯⣭⣤⣤⣾⣿⣤⣤⣤⣶⣾⣿⣤⣴⠾⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⣀⣤⡶⠛⠻⣯⣄⣿⠀⠀⣿⣩⣴⠾⠛⢉⣬⣿⠿⠿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣯⡵⠞⠋⠁⠈⠛⠷⣦⣄⠉⠛⠀⠀⠛⢉⣠⣴⠾⠛⠉⠀⠀⠀⠀⠈⠙⠻⠦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢶⣤⣴⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

WELCOME TO SHINGEKI NO KYOJIN DATABASE

Choose one of the following options
1-Characters Info
2-Titans info
3-Exit

Option Selected: """

opcion = int (input (menu))

menu_characters = True
menu_titans = True

while opcion != 3:
    if opcion == 1:
        page = int (input ("There are 11 pages of characters, please choose a number between 1-11 to display a page?\n"))
        os.system ("cls")
        while menu_characters:
            if page >0 and page <12: #crea un bucle si se ingresa una opcion incorrecta
                get_characters.get_characters_page (page) #llamado de funcion
                id = int (input("Enter the id of the character you want to see: "))
                os.system ("cls")
                for key, value in get_characters.get_character_id (id).items (): #llamado de funcion
                    if key != "episodes" and key != "img" and key != "id": #evita informacion innecesaria
                        print (key.capitalize (),":", value)
                menu_characters = False
            else:
                print ("Please enter a valid number")
                page = int (input ("There are 11 pages of characters, please choose a number between 1-11 to display a page of 20 characters?\n"))
                os.system ("cls")
    elif opcion == 2:
        os.system ("cls")
        print ("List of titans:")
        get_characters.get_titans() #llamado de funcion
        titan = int (input ("Choose the id of the titan you want to see:\n"))
        os.system ("cls")
        while menu_titans:
            if titan >0 and titan <9: #crea un bucle si se ingresa una opcion incorrecta
                for key,value in get_characters.get_titan_id(titan).items(): #llamado de funcion
                    if key != "img" and key != "id": #evita informacion innecesaria
                        print (key.capitalize (),"-", value) 
                menu_titans = False
            else:
                print ("Enter a valid option, between 1-9")
                titan = int (input ("Choose the id of the titan you want to see:\n"))
                os.system ("cls")
    else:
        print ("Enter a valid option")

    time.sleep (5)
    os.system ("cls")
    opcion = int (input (menu))





