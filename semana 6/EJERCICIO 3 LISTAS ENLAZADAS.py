class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.siguiente = None

class Estacionamiento:
    def __init__(self):
        self.cabeza = None

    def agregar_vehiculo(self, placa, marca, modelo, anio, precio):
        nuevo_vehiculo = Vehiculo(placa, marca, modelo, anio, precio)
        if not self.cabeza:
            self.cabeza = nuevo_vehiculo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_vehiculo
        print("Vehículo agregado correctamente.")

    def buscar_vehiculo(self, placa):
        actual = self.cabeza
        while actual:
            if actual.placa == placa:
                return actual
            actual = actual.siguiente
        return None

    def ver_vehiculos_por_anio(self, anio):
        actual = self.cabeza
        vehiculos_anio = []
        while actual:
            if actual.anio == anio:
                vehiculos_anio.append(actual)
            actual = actual.siguiente
        return vehiculos_anio

    def ver_todos_los_vehiculos(self):
        actual = self.cabeza
        if not actual:
            print("No hay vehículos registrados.")
            return
        while actual:
            print(f"Placa: {actual.placa}, Marca: {actual.marca}, Modelo: {actual.modelo}, Año: {actual.anio}, Precio: {actual.precio}")
            actual = actual.siguiente

    def eliminar_vehiculo(self, placa):
        if not self.cabeza:
            print("No hay vehículos registrados.")
            return

        if self.cabeza.placa == placa:
            self.cabeza = self.cabeza.siguiente
            print("Vehículo eliminado correctamente.")
            return

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.placa == placa:
                actual.siguiente = actual.siguiente.siguiente
                print("Vehículo eliminado correctamente.")
                return
            actual = actual.siguiente

        print("No se encontró un vehículo con esa placa.")


# Menú principal
estacionamiento = Estacionamiento()

while True:
    print("\n--- Menú del Estacionamiento ---")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo por placa")
    print("3. Ver vehículos por año")
    print("4. Ver todos los vehículos registrados")
    print("5. Eliminar vehículo")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == '1':
            placa = input("Ingrese la placa: ")
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            anio = int(input("Ingrese el año: "))
            precio = float(input("Ingrese el precio: "))
            estacionamiento.agregar_vehiculo(placa, marca, modelo, anio, precio)
        elif opcion == '2':
            placa = input("Ingrese la placa a buscar: ")
            vehiculo = estacionamiento.buscar_vehiculo(placa)
            if vehiculo:
                print(f"Placa: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}, Precio: {vehiculo.precio}")
            else:
                print("No se encontró un vehículo con esa placa.")
        elif opcion == '3':
            anio = int(input("Ingrese el año a buscar: "))
            vehiculos = estacionamiento.ver_vehiculos_por_anio(anio)
            if vehiculos:
                for vehiculo in vehiculos:
                    print(f"Placa: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}, Precio: {vehiculo.precio}")
            else:
                print(f"No se encontraron vehículos del año {anio}.")
        elif opcion == '4':
            estacionamiento.ver_todos_los_vehiculos()
        elif opcion == '5':
          placa = input("Ingrese la placa del vehículo a eliminar: ")
          estacionamiento.eliminar_vehiculo(placa)
        elif opcion == '6':
            break
        else:
            print("Opción inválida. Intente de nuevo.")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para el año o el precio.")