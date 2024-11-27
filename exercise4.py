amount = float(input("Ingrese la cantidad de la inversion:"))
interest = float(input("Ingrese el interest anual:"))


result = amount + (amount * (interest / 100))

print("El capital obtenido en la inversion es de:", result)
