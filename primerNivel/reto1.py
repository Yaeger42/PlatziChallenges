'''
Reto #1 “Hola Mundo”
Instrucciones: este es un clásico de clásicos, 
pero haremos un pequeño cambio. 
En lugar de solo imprimir un mensaje en pantalla, 
pedirás al usuario que digite un nombre y mostrarás 
en pantalla lo siguiente: Hola, [nombre]
'''
def sayHello():
    name = input("Enter your name: ")
    return print(f"Hello {name}")
sayHello()