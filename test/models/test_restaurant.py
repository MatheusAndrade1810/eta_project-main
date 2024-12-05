from src.models.restaurant import Restaurant

class TestRestaurant:

    def test_describe_restaurant(self):
        restaurante = Restaurant('Cuscuz','comida nordestina')

        resultado = restaurante.describe_restaurant()
        resultado_esperado = ('Esse restaurante chama Cuscuz e serve comida nordestina. Esse restaurante está servindo 0 consumidores desde que abriu.')
        assert resultado == resultado_esperado

    #funcionou
    def test_describe_restaurant_name_empty(self):
        restaurante = Restaurant('', 'comida nordestina')

        resultado = restaurante.describe_restaurant()
        resultado_esperado = ('Erro: O nome do restaurante está vazio.')

        assert resultado == resultado_esperado

    # não conseguimos verificar esse
    def test_describe_restaurant_name_is_none(self):
        restaurante = Restaurant(None, 'comida nordestina')

        resultado = restaurante.describe_restaurant()
        resultado_esperado = ('Erro: O nome do restaurante está vazio.')

        assert resultado == resultado_esperado

    #funcionou
    def test_describe_restaurant_cuisine_type_empty(self):
        restaurante = Restaurant('Cuscuz', '')

        resultado = restaurante.describe_restaurant()
        resultado_esperado = ('Erro: O tipo de culinária está vazio.')

        assert resultado == resultado_esperado

    #funcionou
    def test_describe_restaurant_cuisine_type_is_none(self):
        restaurante = Restaurant('Cuscuz', None)

        resultado = restaurante.describe_restaurant()
        resultado_esperado = ('Erro: O tipo de culinária está vazio.')

        assert resultado == resultado_esperado

    def test_describe_restaurant_cuisine_number_served_not_int(self):
        restaurante = Restaurant('Cuscuz', 'comida nordestina')
        #como vamos mandara o numero se não é chamado no construtor?

        restaurante.number_served = "chocolate"

        resultado_esperado = ('Erro: O número de consumidores deve ser um inteiro não negativo.')

        assert restaurante.describe_restaurant() == resultado_esperado

    def test_describe_restaurant_cuisine_number_served_negative(self):
        restaurante = Restaurant('Cuscuz', 'comida nordestina')

        restaurante.number_served = -1
        resultado_esperado = ('Erro: O número de consumidores deve ser um inteiro não negativo.')

        assert restaurante.describe_restaurant() == resultado_esperado

    def test_describe_restaurant_cuisine_number_served_is_none(self):
        restaurante = Restaurant('Cuscuz', 'comida nordestina')
        restaurante.number_served = None
        resultado_esperado = ('Erro: O número de consumidores deve ser um inteiro não negativo.')

        assert restaurante.describe_restaurant() == resultado_esperado

    def test_open_restaurant(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')

        restaurante.open = True
        resultado_esperado = ('Restaurante Cuscuz agora está aberto!')
        assert restaurante.open_restaurant() == resultado_esperado
        #estou na dúvida se a lógica desse teste e do teste abaixo estão corretas. Me parece q é o contrário

    def test_restaurant_alredy_open(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')

        restaurante.open = False
        resultado_esperado = ('Restaurante Cuscuz já está aberto!')
        assert restaurante.open_restaurant() == resultado_esperado

    def test_close_restaurant(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')

        restaurante.open = True
        resultado_esperado = ('Restaurante Cuscuz agora está fechado!')
        assert restaurante.close_restaurant() == resultado_esperado

    def test_restaurant_alredy_close(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')

        restaurante.open = False
        resultado_esperado = ('Restaurante Cuscuz já está fechado!')
        assert restaurante.close_restaurant() == resultado_esperado

    def test_set_number_served(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')
        restaurante.open = True
        total_customers = 25
        restaurante.set_number_served(total_customers)
        resultado_esperado = ('A quantidade de cliente é de: 25')
        assert restaurante.set_number_served(total_customers) == resultado_esperado

    def test_set_number_not_served(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')
        total_customers = 25
        restaurante.set_number_served(total_customers)
        resultado_esperado = ('Restaurante Cuscuz está fechado!')
        assert restaurante.set_number_served(total_customers) == resultado_esperado

    def test_set_negative_number_diferent_int(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')
        total_customers = 'Cris'
        restaurante.set_number_served(total_customers)
        resultado_esperado = ('Quantidade de cliente não pode ser negativo e precisa ser um valor inteiro!')
        assert restaurante.set_number_served(total_customers) == resultado_esperado

    def test_set_negative_number_served(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')
        total_customers = -1
        restaurante.set_number_served(total_customers)
        resultado_esperado = ('Quantidade de cliente não pode ser negativo e precisa ser um valor inteiro!')
        assert restaurante.set_number_served(total_customers) == resultado_esperado

    def test_increment_number_diferente_int(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')

        more_customers = 'Cris'
        restaurante.increment_number_served(more_customers)
        resultado_esperado = ('Quantidade de cliente não pode ser negativo e precisa ser um valor inteiro!')
        assert restaurante.increment_number_served(more_customers) == resultado_esperado

    def test_increment_negative_number(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')

        more_customers = -1
        restaurante.increment_number_served(more_customers)
        resultado_esperado = ('Quantidade de cliente não pode ser negativo e precisa ser um valor inteiro!')
        assert restaurante.increment_number_served(more_customers) == resultado_esperado

    def test_increment_number_served(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')
        restaurante.open = True
        more_customers = 100
        resultado_esperado = ('O novo número total de cliente é: 100')
        assert restaurante.increment_number_served(more_customers) == resultado_esperado

    def test_increment_number_not_served(self):
        restaurante = Restaurant('Restaurante Cuscuz', 'comida nordestina')
        more_customers = 100
        resultado_esperado = ('Restaurante Cuscuz está fechado!')
        assert restaurante.increment_number_served(more_customers) == resultado_esperado

