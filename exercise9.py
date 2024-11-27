name = str(input("Ingrese su nombre:"))
subject = str(input("Ingrese la asignatura:"))

percentages = [0.30, 0.30, 0.40]
finalNote = 0

i = 1
while i <= 3:
    note = float(input("Ingrese el valor de la nota #" + str(i) + ":"))

    if note <= 5 and note >= 0:
        finalNote += note * percentages[i - 1]
        i += 1
    else:
        print("El valor de la nota debe estar entre 0 y 5.")

if finalNote >= 4:
    print("El aprendiz", name, " aprobo", subject, " con", finalNote)
else:
    print("El aprendiz", name, " reprobo", subject, " con", finalNote)
