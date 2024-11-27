quantity = int(input("Ingrese la cantidad de notas:"))
i = 1

notes = 0
average = 0
while i <= quantity:
    note = float(input("Ingrese el valor de la nota #" + str(i) + ":"))

    if note <= 5 and note >= 0:
        notes += note
        i += 1
    else:
        print("El valor de la nota debe estar entre 0 y 5.")

average = notes / quantity
if average >= 4.5:
    print("Aprobo la asignatura con", average)
else:
    print("No aprobo la asignatura con", average)
