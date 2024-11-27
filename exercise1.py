number = int(input("Ingrese un numero:"))
result = number

i = 0
for i in range(1, number):
    result = result * i

print("El factorial del numero", number, "es", result)
