# Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))

# Invertir la lista
numeros_invertidos = numeros[::-1]

# Mostrar los números separados por comas
print(", ".join(map(str, numeros_invertidos)))