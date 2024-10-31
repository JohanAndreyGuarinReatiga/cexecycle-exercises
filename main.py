# Múltiplos
#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:


while True:
    number = int(input("Type your number: "))
    for multiple in range(1, 11):
        print(f"""
      {number} * {multiple} = {number * multiple}
      """)
    confirmation = input("Do you want to continue? Type 'yes' to continue or 'no' to end the program: ")
    if confirmation == 'no':
        print("Program ended.")
        break
    elif confirmation == 'yes':
        continue
