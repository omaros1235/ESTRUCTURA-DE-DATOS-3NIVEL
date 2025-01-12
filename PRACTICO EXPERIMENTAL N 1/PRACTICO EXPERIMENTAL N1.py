class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"

class AgendaTelefonica:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, correo):
        nuevo_contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo_contacto)
        print("Contacto agregado correctamente.")

    def buscar_contacto(self, nombre):
        resultados = [contacto for contacto in self.contactos if nombre.lower() in contacto.nombre.lower()]
        if resultados:
            print("\nContactos encontrados:")
            for contacto in resultados:
                print(contacto)
        else:
            print("No se encontraron contactos con ese nombre.")

    def eliminar_contacto(self, nombre):
        contactos_a_eliminar = [contacto for contacto in self.contactos if nombre.lower() in contacto.nombre.lower()]
        if contactos_a_eliminar:
            for contacto in contactos_a_eliminar:
                self.contactos.remove(contacto)
            print(f"{len(contactos_a_eliminar)} contacto(s) eliminado(s) correctamente.")
        else:
            print("No se encontraron contactos para eliminar.")

    def mostrar_todos(self):
        if self.contactos:
            print("\nLista de contactos:")
            for contacto in self.contactos:
                print(contacto)
        else:
            print("La agenda está vacía.")

def main():
    agenda = AgendaTelefonica()

    while True:
        print("\n************************* UNIVERSIDAD ESTATAL AMAZONICA *******************************")
        print("************************ FACULTAD DE CIENCIAS DE LA EDUCACION **************************")
        print("********************* INTEGRANTE DEL TRABAJO PRACTICO EXPERIMENTAL ********************")
        print("")
        print("SR. KLEBER OMAR MORALES LOPEZ")
        print("\n********************* AGENDA TELEFONICA ***********************************")
        print("*********************** 1. Agregar contacto ***********************************")
        print("*********************** 2. Buscar contacto ************************************")
        print("*********************** 3. Eliminar contacto ***********************************")
        print("*********************** 4. Mostrar todos los contactos **************************")
        print("*********************** 5. Salir **********************************************")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Agregar Contacto ---")
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            correo = input("Ingrese el correo: ")
            agenda.agregar_contacto(nombre, telefono, correo)
            input("Presione Enter para continuar...") # Simula Console.ReadKey()
        elif opcion == "2":
            print("\n--- Buscar Contacto ---")
            nombre = input("Ingrese el nombre a buscar: ")
            agenda.buscar_contacto(nombre)
            input("Presione Enter para continuar...")
        elif opcion == "3":
            print("\n--- Eliminar Contacto ---")
            nombre = input("Ingrese el nombre a eliminar: ")
            agenda.eliminar_contacto(nombre)
            input("Presione Enter para continuar...")
        elif opcion == "4":
            print("\n--- Mostrar Todos los Contactos ---")
            agenda.mostrar_todos()
            input("Presione Enter para continuar...")
        elif opcion == "5":
            print("\nSaliendo de la agenda. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()