from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list if flavors_list else []

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            result = "No momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                result += f"{flavor}"

            return result
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if flavor in self.flavors:
            return f"Temos {flavor} no estoque!"
        else:
            return f"Não temos {flavor} no momento!"
        # BUG 5: A lista de sabores "self.flavors" que estava sendo trazidas nos retornos.
        # Coreção: O flavor que foi passado é que deve ser trazido nos retornos.

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""

        if flavor in self.flavors:
            return "Sabor já disponivel!"
        else:
             self.flavors.append(flavor)
             return f"{flavor} adicionado ao estoque!"
