'''
Reto #9 “Calculando días”
Instrucciones: escribe un programa al que le indiques una 
cantidad de días y como resultado deberá mostrar cuantas 
horas, minutos y segundos hay en dicha cantidad de días.
'''
def quantityOfDays(days):
    hours = int(days * 24)
    minutes = int(hours * 60)
    seconds = int(minutes * 60)
    return print(hours, minutes, seconds)
quantityOfDays(2)
