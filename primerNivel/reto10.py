'''
Reto #10 “Conversor de millas”
Instrucciones: hay 1.609344 km en una milla (mi). 
Escribe un programa en el que el usuario indique una cantidad de millas 
y muestre en pantalla el resultado convertido a kilómetros.
'''

def fromMtoKm():
    miles = float(input("Enter the total of miles: "))
    km = float(1.609344 * miles)
    return print("The total kilometers is: " + str(km))
    
fromMtoKm()