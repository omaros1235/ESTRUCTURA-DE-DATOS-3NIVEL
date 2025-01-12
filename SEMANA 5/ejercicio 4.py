# Pedir al usuario los 6 números ganadores
print("Introduce los números ganadores de la lotería primitiva:")

numeros_ganadores = []  # Inicializar la lista fuera del bucle

for i in range(6):
    while True: # Bucle para validación de entrada
        try:
            numero = int(input(f"Introduce el número {i + 1}: "))
            if 1 <= numero <= 49 and numero not in numeros_ganadores: #Validar que el número esté entre 1 y 49 y que no se repita
                numeros_ganadores.append(numero)
                break # Sale del bucle while si la entrada es correcta
            elif numero in numeros_ganadores:
                print("Este número ya ha sido introducido. Por favor, introduce un número diferente.")
            else:
                print("Por favor, introduce un número entre 1 y 49.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")


# Ordenar la lista de menor a mayor
numeros_ganadores.sort()

# Mostrar los números ganadores ordenados
print("\nLos números ganadores ordenados de menor a mayor son:")
print(numeros_ganadores)