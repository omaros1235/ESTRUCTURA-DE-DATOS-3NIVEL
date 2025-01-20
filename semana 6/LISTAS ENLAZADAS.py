class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def buscar(self, valor):
        """
        Busca un valor en la lista y retorna el número de veces que aparece.

        Args:
            valor: El valor a buscar.

        Returns:
            int: El número de veces que aparece el valor en la lista.
                 Retorna un mensaje indicando que no se encontró si no está.
        """
        contador = 0
        for elemento in self.elementos:
            if elemento == valor:
                contador += 1

        if contador == 0:
            return f"El valor {valor} no fue encontrado en la lista."
        else:
            return contador

# Ejemplos de uso
lista1 = Lista([1, 2, 3, 4, 2, 5, 2])
resultado1 = lista1.buscar(2)
print(f"El valor 2 aparece {resultado1} veces.")  # Salida: El valor 2 aparece 3 veces.

lista2 = Lista(["manzana", "banana", "pera", "banana"])
resultado2 = lista2.buscar("banana")
print(f"El valor 'banana' aparece {resultado2} veces.") # Salida: El valor 'banana' aparece 2 veces.

lista3 = Lista([10, 20, 30])
resultado3 = lista3.buscar(40)
print(resultado3)  # Salida: El valor 40 no fue encontrado en la lista.

lista4 = Lista([]) #Lista vacia
resultado4 = lista4.buscar(5)
print(resultado4) # Salida: El valor 5 no fue encontrado en la lista.