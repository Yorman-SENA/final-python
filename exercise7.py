name = str(input("Ingrese su nombre:"))
subject = str(input("Ingrese la asignatura:"))
note = float(input("Ingrese la calificación final:"))

if note <= 10 and note >= 1:
    if note >= 7:
        print("Aprobo la asignatura con", note)
    elif note < 7:
        print("No aprobo la asignatura con", note)
else:
    print("El valor de la nota debe estar entre 1 y 10.")
