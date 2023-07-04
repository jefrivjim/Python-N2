valido = False

email = input ("ingrese su email: ")

for x in email:
    if x == "@":
        valido = True

if valido == True:
    print ("el email es correcto")
else:
    print ("ingrese un email correcto")
    
