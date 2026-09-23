import math
n = int(input("Masukkan nilai n: "))

limit = math.factorial(n)

a, b = 0, 1

print(f"Deret Fibonacci hingga n! ({n}! = {limit}):")

while a <= limit:
    print(a, end=" ")
    a, b = b, a + b