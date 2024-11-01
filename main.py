#π
#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita

n = int(input("Enter the number: "))

piNum = 0
for term in range(n):
    piNum += (-1) ** term / (2 * term + 1)
piNum *= 4
print(f"The approximation of pi with {n} terms is: {piNum}")
