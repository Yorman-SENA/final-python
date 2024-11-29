import os

option = ""


def importFile(option):
    file_name = f"exercise{option}.py"
    if os.path.exists(file_name):
        exec(open(file_name).read())
    else:
        print(f"{file_name} does not exist.")


while option != "exit":
    option = input(
        "¿Cual ejercicio desea ejecutar? (1, 2, 3, 4, 5, 6, 7, 8, 9, 19 exit): "
    )
    if option == "exit":
        break
    importFile(option)
