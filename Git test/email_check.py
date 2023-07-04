valido = False
email = input ("ingrese su email: ")

for x in email:
    if x == "@":
        valido == True

if valido == True:
    print ("email correcto")
else:
    print ("ingrese un email correcto")


            



