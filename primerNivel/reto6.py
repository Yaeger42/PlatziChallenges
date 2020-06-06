'''
Reto #6 “Resta de pizzas”
Instrucciones: llegaste a una fiesta con X cantidad de rebanadas de pizza
(indicadas por el usuario), después de un rato se consumió Y cantidad de 
rebanadas y quedan Z. Fácil ¿cierto?
El reto está en que expreses lo que sucede es una forma comprensible 
para cualquier persona, imprescindible pensar en tus usuarios 😉
'''
def pizzaTime():
    x = int(input("Enter the number of total slices: "))
    y = int(input("Enter the number of consumed slices: "))
    z = x - y
    return z 
pizzaTime()