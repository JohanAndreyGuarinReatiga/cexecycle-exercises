#Dibujos de asteriscos


print("Select the shape you want to draw:")
print("1. Rectangle")
print("2. Triangle")
print("3. Hexagon")
choice = int(input("Enter the number of your choice: "))
if choice == 1:
    height = int(input("Enter the height of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    
    print("\nRectangle:")
    for nnn1 in range(height):
        print("*" * width)

elif choice == 2:
    height = int(input("Enter the height of the triangle: "))
    
    print("\nTriangle:")
    for lineNum in range(1, height + 1):
        print("*" * lineNum)

elif choice == 3:
    sideLength = int(input("Enter the side length of the hexagon: "))
    
    print("\nHexagon:")
    for lineNum in range(1, sideLength + 1):
        print(" " * (sideLength - lineNum) + "*" * (sideLength + 2 * (lineNum - 1)))
    
    for lineNum in range(sideLength - 1, 0, -1):
        print(" " * (sideLength - lineNum) + "*" * (sideLength + 2 * (lineNum - 1)))

else:
    print("Invalid option. Please choose between 1, 2, and 3.")

