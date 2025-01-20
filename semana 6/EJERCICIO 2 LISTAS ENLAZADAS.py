import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def eliminar_fuera_de_rango(self, minimo, maximo):
        if not self.cabeza:
            return

        # Eliminar nodos al principio de la lista
        while self.cabeza and (self.cabeza.dato < minimo or self.cabeza.dato > maximo):
            self.cabeza = self.cabeza.siguiente

        if not self.cabeza: #Si la lista queda vacia despues de eliminar los primeros nodos
            return

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato < minimo or actual.siguiente.dato > maximo:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

# Crear la lista enlazada con 50 números aleatorios
mi_lista = ListaEnlazada()
for _ in range(50):
    numero_aleatorio = random.randint(1, 999)
    mi_lista.agregar(numero_aleatorio)

print("Lista original:")
mi_lista.imprimir()

# Leer el rango desde el teclado
try:
    minimo = int(input("Ingrese el valor mínimo del rango: "))
    maximo = int(input("Ingrese el valor máximo del rango: "))
    if minimo > maximo:
      print("El valor minimo no puede ser mayor al valor maximo.")
    else:
      # Eliminar nodos fuera del rango
      mi_lista.eliminar_fuera_de_rango(minimo, maximo)

      print("\nLista después de eliminar nodos fuera del rango:")
      mi_lista.imprimir()
except ValueError:
    print("Por favor, ingrese números enteros válidos.")