"""
Pide salario y clasifica el cargo
<1000 junior
1000-2000 semi senior
>2000 senior

"""

salario = float(input("Ingrese el salario del empleado:"))
if 1000 <= salario <= 2000:
    cargo = "Semi Senior"
elif salario > 2000:
    cargo = "Senior"
else:
    cargo = "Junior"
print(f"El empleado es: {cargo}")
