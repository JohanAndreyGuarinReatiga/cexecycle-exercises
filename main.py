#Secuencia de Collatz
#

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def print_collatz_lengths(limit):
    for i in range(1, limit + 1):
        sequence = collatz_sequence(i)
        length = len(sequence)
        print(f"{i} {'*' * length}")

n = int(input("Enter an integer number: "))

for i in range(1, n + 1):
    sequence = collatz_sequence(i)
    print(f"n: {i}")
    print(" ".join(map(str, sequence)))

print("\nGráfico de los largos de las secuencias de Collatz:")
print_collatz_lengths(n)
