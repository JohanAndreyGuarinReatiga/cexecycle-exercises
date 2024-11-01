#Tabla de multiplicar


maxNumber = 10

for spc in range(1, maxNumber + 1):
    print(f"{spc:>3}", end=" ")  
print()  
for spc in range(1, maxNumber + 1):
    for hor in range(1, maxNumber + 1):
        print(f"{spc * hor:>3}", end=" ")  
    print()
