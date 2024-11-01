#Suma entre números
#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos.

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

if firstNumber > secondNumber:
    firstNumber, secondNumber = secondNumber, firstNumber 

totalSum = 0
for number in range(firstNumber + 1, secondNumber):
    totalSum += number
print(f"The sum is {totalSum}")
