n = int(input("Enter n value: "))

print()  

for i in range(1, n + 1):
    print(" ".join([str(i)] * i))
    print()