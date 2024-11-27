total = float(input('Ingrese el total:'))

discount = 0.20

if total > 20000:
    print('El valor a pagar es ', total - (total * discount))
else:
    print('El valor a pagar es ', total)