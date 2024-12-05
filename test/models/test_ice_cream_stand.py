from src.models.ice_cream_stand import IceCreamStand
from src.models.restaurant import Restaurant

class TestIceCreamStand:

    def test_flavors_available(self):
        # Crie a instância passando os argumentos necessários
        iceCreamStand = IceCreamStand("Sorvetes do Brasil", "Sorvetes", ["chocolate", "amendoim"])

        resultado = iceCreamStand.flavors_available()
        resultado_esperado = ('No momento temos os seguintes sabores de sorvete disponíveis: chocolate, amendoim')

        assert resultado == resultado_esperado

    def test_flavors_not_available(self):
        pass

    def test_find_flavor(self):
        # Crie a instância passando os argumentos necessários
        iceCreamStand = IceCreamStand("Sorvetes do Brasil", "Sorvetes", ["caja", "amendoim"])

        resultado = iceCreamStand.find_flavor('caja')
        resultado_esperado = ('Temos caja no estoque!')

        assert resultado == resultado_esperado

    def test_donot_find_flavor(self):
        # Crie a instância passando os argumentos necessários
        iceCreamStand = IceCreamStand("Sorvetes do Brasil", "Sorvetes", ["caja", "amendoim"])

        resultado = iceCreamStand.find_flavor('limao')
        resultado_esperado = ('Não temos limao no momento!')

        assert resultado == resultado_esperado


    def test_add_flavor(self):
        # Crie a instância passando os argumentos necessários
        iceCreamStand = IceCreamStand("Sorvetes do Brasil", "Sorvetes", ["jaca", "amendoim"])

        # Adicione um novo sabor
        resultado = iceCreamStand.add_flavor("morango")
        resultado_esperado = ("morango adicionado ao estoque!")

        # Teste se o sabor foi adicionado corretamente
        assert resultado == resultado_esperado


    def test_add_flavor_existent(self):
        # Crie a instância passando os argumentos necessários
        iceCreamStand = IceCreamStand("Sorveteria do Brasil", "Sorvetes", ["morango", "amendoim"])

        # Adicione um novo sabor
        resultado = iceCreamStand.add_flavor("morango")
        resultado_esperado = ("Sabor já disponivel!")

        # Verificar que sabor ja existe
        assert resultado == resultado_esperado