"""
Escribe un programa que pida edad, años de experiencia y si tiene
titulo universitario.
Un candidato es elegible si tiene >= 21 años y experiencia >=2 años o titulo.
Muestra Elegible o No Elegible
"""

edad = int(input("Edad del candidato: "))
exp = float(input("Años de experiencia: "))
tiene_titulo = input("¿Tiene título universitario? (s/n): ").strip().lower() == "s"

# Evaluación
if edad >= 21 and (exp >= 2 or tiene_titulo):
    print("El candidato es ELEGIBLE.")
else:
    print("El candidato NO es elegible.")