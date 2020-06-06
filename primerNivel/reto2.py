'''
Reto #2 “Hola… nombre y apellido:”
Instrucciones: Ahora que sabemos 
incluir nombres, podemos agregar 
más datos. 
Intentemos con un apellido para tener algo así: ``Hola, [nombre] [apellido]```
'''
def sayHello2()
    name = str(input("Enter your name: "))
    lastName = str(input("Enter your last name: "))
    return print("Hello "+ name + " " + lastName)
sayHello2()