rate = 3934
condition = "si"
while condition == "si":
    quantity = float(input("Ingrese la cantidad en dolares:"))
    print("La cantidad en pesos es:", quantity * rate)

    condition = str(input("¿Desea seguir convirtiendo?"))
