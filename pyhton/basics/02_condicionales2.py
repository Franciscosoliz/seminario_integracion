"""
Sitema que pida pago por hora y horas trabajadas.
Las primeras 40h son normales, las extras se pagan al 150%.
Calcula y muestra el total semanal.

"""
pago = float(input("Ingrese el pago por hora: "))
horas = float(input("Ingrese las horas trabajadas: "))

if horas <= 40:
    total = pago * horas
else:
    horas_extras = horas - 40
    total = (pago * 40) + (pago * 1.5 * horas_extras)

print(f"El total semanal a pagar es: ${total:.2f}")
