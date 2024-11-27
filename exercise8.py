gender = str(input('Ingrese el genero F/M:'))
age = int(input('Ingrese la edad:'))

minimumAgeFemale = 54
minimumAgeMale = 63

gender = gender.upper()

if gender != 'F' and gender != 'M':
    print('Genero incorrecto.',gender)
elif (gender == 'F' and age > minimumAgeFemale) or (gender == 'M' and age >= minimumAgeMale):
    print('¡Ya puedes julibarte!')
else:
    print('¡Aun no puedes julibarte! :C')
    