class Atraccion:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = []  # Lista para simular la cola de espera

    def subir_a_atraccion(self, nombre_persona):
        if len(self.cola) < self.capacidad:
            self.cola.append(nombre_persona)
            print(f"{nombre_persona} ha subido a la atracción.")
        else:
            print("Lo siento, la atracción está llena.")

# Ejemplo de uso
atraccion = Atraccion(30)

atraccion.subir_a_atraccion("Juan")
atraccion.subir_a_atraccion("María")
# ... (seguir agregando personas)

# Cuando la cola esté llena:
atraccion.subir_a_atraccion("Pedro")  # No podrá subir