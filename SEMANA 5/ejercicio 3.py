# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Diccionario para almacenar las notas
notas = {}

# Pedir al usuario la nota para cada asignatura
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas[asignatura] = nota

# Mostrar las asignaturas y notas
print("\nTus notas son:")


for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")