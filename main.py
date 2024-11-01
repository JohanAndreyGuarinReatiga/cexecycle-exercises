#Tiempo de viaje¶
#Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.

#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.

#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

totalMin = 0

while True:
    duration = int(input("Duration (in minutes, enter 0 to finish): "))
    if duration == 0:  
        break
    totalMin += duration  

hours = totalMin // 60
minutes = totalMin % 60

print(f"Total travel time: {hours}:{minutes:02d} hours")
