#suma de fracciones 
#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos

print("Power\tFraction\tSum")

power = 1
fraction = 0.5
sumAc = 0

while fraction > 0.000001:
    sumAc += fraction
    print(f"{power}\t{fraction:.6f}\t{sumAc:.6f}")
    power += 1
    fraction /= 2
