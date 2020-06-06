'''
Reto #11 “Cuantas veces un número en otro”
Instrucciones: pide al usuario ingresar un número mayor a 1000 
y otro menor a 100. Indica de una forma sencilla de entender al 
usuario cuantas veces cabe el número menor a 100 en el número mayor a 1000
'''

def howManyTimes():
    x = int(input("Enter a number greater than 1000: "))
    y = int(input("Now enter a number smaller than 100: "))
    if x < 1000 and y > 1000:
        print("I said greater than 1000")
    else:
        z = x / y 
    print("If you multiply the number smaller than 100 enough times by itself\
        eventualy you'll be able to make it equal than the one greater than 1000\
            however, if you can't make it equal to the other number you'll get\
                close enough without passing its value. Given that\
                    the result is: " + str(z))
howManyTimes()

    