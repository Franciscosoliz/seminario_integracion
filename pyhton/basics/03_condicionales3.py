"""
Vacacciones por antiguedad
Pide años de antiguedad y muestra los dias de vacaciones
<1 = 0
<3 = 3
<5 = 10
>=5 = 15

"""

antiguedad = float(input("Ingrese los años de antigüedad del empleado: "))

if antiguedad < 1:
    dias = 0
elif antiguedad < 3:
    dias = 3
elif antiguedad < 5:
    dias = 10
else:
    dias = 15

print(f"El empleado tiene derecho a {dias} días de vacaciones.")