import math

class Circulo:
    def __init__(self, radio):
        self.__radio = radio  # Encapsulamos el atributo

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * self.__radio ** 2

    def calcular_perimetro(self):
        """Calcula el perímetro del círculo."""
        return 2 * math.pi * self.__radio

    @property
    def radio(self):
        """Getter para el radio."""
        return self.__radio

    @radio.setter
    def radio(self, radio):
        """Setter para el radio."""
        if radio > 0:
            self.__radio = radio
        else:
            raise ValueError("El radio debe ser mayor que 0")


class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base  # Encapsulamos el atributo base
        self.__altura = altura  # Encapsulamos el atributo altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.__base * self.__altura

    def calcular_perimetro(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.__base + self.__altura)

    @property
    def base(self):
        """Getter para la base."""
        return self.__base

    @base.setter
    def base(self, base):
        """Setter para la base."""
        if base > 0:
            self.__base = base
        else:
            raise ValueError("La base debe ser mayor que 0")

    @property
    def altura(self):
        """Getter para la altura."""
        return self.__altura

    @altura.setter
    def altura(self, altura):
        """Setter para la altura."""
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("La altura debe ser mayor que 0")

# Ejemplo de uso
if __name__ == "__main__":
    # Círculo
    circulo = Circulo(5)
    print(f"Área del círculo: {circulo.calcular_area():.2f}")
    print(f"Perímetro del círculo: {circulo.calcular_perimetro():.2f}")

    # Rectángulo
    rectangulo = Rectangulo(4, 7)
    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")