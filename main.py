#Potencias de dos
#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
import math

while True:
    quantity = int(input("""
 Enter the maximum exponent for powers of 2:  """))
    
    if quantity >= 0:
        for exponent in range(quantity + 1):
            print(int(math.pow(2, exponent)), end=" ")
