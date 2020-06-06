'''
Reto #5 “Suma y multiplicación”
Instrucciones: añadiendo un extra al reto anterior ahora 
el usuario ingresará 3 números, sumarás los 2 primeros y 
el resultado será multiplicado por el tercero. Añade las consideraciones 
del punto decimal del reto anterior.
Ejemplo:
Datos de entrada:2, 3, 4
Resultado:20
'''
from decimal import *

def integerSum2():
    int1 = Decimal(input("Enter the first number: "))
    int2 = Decimal(input("Enter the second number: "))
    int3 = int(input("Enter the third number: "))
    decimals = int(input("Enter how many decimals you want: "))
    x = getcontext().prec = c+1
    result = (int1 + int2) * int3 
    return print(result)

integerSum2()