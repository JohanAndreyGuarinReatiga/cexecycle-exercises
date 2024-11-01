#e 
#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.


from math import factorial

eValue = 1.0
num = 1
termim = 1.0    

while termim > 0.0001:
    termim = 1 / factorial(num)
    eValue += termim
    num += 1

print(f"Approximation of e: {eValue}")

