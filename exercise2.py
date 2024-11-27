initialNumber = int(input("Ingrese el numero inicial del rango:"))
finalNumber = int(input("Ingrese el numero final del rango:"))

i = 0
for i in range(initialNumber, finalNumber):
    if i % 2 != 0:
        print(
            "El numero",
            i,
            " es impar",
        )
