"""
Pide el numero de empleados y luego el sueldo de cada uno
Suma y muestra la nomina total

"""
empleados = int(input("Cuantos empleados tiene la empresa?"))
nomina = 0
for i in range(empleados):
    sueldo = float(input(f"Sueldo del empleado {i+1}: "))
    nomina += sueldo
print(f"La nomina total es: ${nomina:.2f}")
