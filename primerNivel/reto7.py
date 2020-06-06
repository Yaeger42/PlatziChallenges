'''
Reto #7 “Edad futura y pasada”
Instrucciones: pide al usuario que indique su nombre 
y su edad. Como mensaje de salida le indicarás que edad 
tuvo el año pasado y cuantos años tendrá el siguiente año.
Ejemplo: [nombre] el año pasado tenías X años y el próximo año cumplirás Y años.
'''


def birthdays():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    past = age - 1
    future = age + 1
    return print(name + " " + "You'll be " +  str(future) + " years old in one year and you were " 
    + str(future) + " years old one year ago")

birthdays()
 