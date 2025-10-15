"""
Pide numero de empleados
Cada empleado solicita nombre y salario
determina quien tiene el mayor salario y muestralo

"""

num_empleados = int(input("Ingrese el número de empleados: "))

contador = 1
mayor_salario = 0
empleado_mayor = ""

while contador <= num_empleados:
    print(f"\nEmpleado {contador}:")
    nombre = input("Nombre del empleado: ")
    salario = float(input("Salario del empleado: "))

    if salario > mayor_salario:
        mayor_salario = salario
        empleado_mayor = nombre

    contador += 1

print("\n--- RESULTADO ---")
print(f"El empleado con mayor salario es {empleado_mayor} con un salario de ${mayor_salario:.2f}")
