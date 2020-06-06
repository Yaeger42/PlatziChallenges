'''
Reto #4 “Suma de enteros”
Instrucciones: otro clásico conocido, donde pedirás 
al usuario que ingrese 2 números y muestre en pantalla
el resultado. Si quieres añadir más dificultad 
puedes utilizar números con punto decimal y especificar 
el número de decimales después del punto.
Ejemplo: 2.5633 + 5.6883 = 8.25
'''
from decimal import *
def integerSum():
    a = Decimal(input("Enter the first number: "))
    b = Decimal(input("Enter the second number: "))
    c = int(input("Enter how many decimals you want: "))
    x = getcontext().prec = c+1
    result = a + b
    return print(result)
integerSum()