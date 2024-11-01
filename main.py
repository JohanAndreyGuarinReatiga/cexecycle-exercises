#Divisores¶
#Escriba un programa que entregue todos los divisores del número entero ingresado:

number = int(input("Enter a number: "))
divisors = []
for div in range(1, number + 1):
    if number % div == 0: 
        divisors.append(div)
        
print("Divisors:", " ".join(map(str, divisors)))
