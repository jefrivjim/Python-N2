import pandas as pd
import matplotlib.pyplot as plt

#Carga el archivo excel, debe estar en la misma carpeta que el archivo py
df = pd.read_csv ("ventas.csv")

#Crea una nueva columna con el nombre Ganancia, resultado de restar los Gastos a las Ventas
df["Ganancia"] = df["Ventas"] - df["Gastos"]
#print (df)

#Creacion de grafico de lineas, basado en Ventas y Gastos por mes
mes = df["Mes"]
ventas = df["Ventas"]
gastos = df["Gastos"]

fig, ax = plt.subplots ()
ax.plot (mes, ventas, color = "tab:purple", label = "Ventas") #crea la linea para Ventas
ax.plot (mes, gastos, color = "tab:green", label = "Gastos") #crea la linea para Gastos
ax.set_title ("Evolucion Mensual") #agrega titulo
ax.set_xlabel("Mes") #agrega etiqueta a eje X
ax.set_ylabel ("Ventas/Gastos") #agrega etiqueta a eje Y
ax.legend() #agrega la leyenda añadida anteriormente
plt.show () 


