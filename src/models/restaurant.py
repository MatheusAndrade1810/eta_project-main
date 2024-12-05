class Restaurant:
    """Modelo de restaurante simples"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Inicializa os atributos da classe Restaurant.
        """
        if restaurant_name:
            self.restaurant_name = restaurant_name.title()
        else:
            self.restaurant_name = ""

        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """
        Retorna uma descrição simples do restaurante.
        """
        if not self.restaurant_name or self.restaurant_name is None:
            return "Erro: O nome do restaurante está vazio."

        if not self.cuisine_type or self.cuisine_type is None:
            return "Erro: O tipo de culinária está vazio."

        if not isinstance(self.number_served, int) or self.number_served < 0 or self.number_served is None:
            return "Erro: O número de consumidores deve ser um inteiro não negativo."
        # REFATORAÇÃO 1: Não existia validação para entrada vazia, nas três variáveis e não verificava se o valor number_serverd era inteiro.
        # Alterações: Adicionado um if para não aceitar valor vazio e diferente de inteiro

        # BUG 1: O nome do restaurant não estava sendo passado corretamente.
        #Correção: Foi ajustado de "self.cuisine_type" para "self.restaurant_name"
        result = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}."
        result += f" Esse restaurante está servindo {self.number_served} consumidores desde que abriu."
        return result

    def open_restaurant(self):
        """
        Imprima uma mensagem indicando que o restaurante está aberto para negócios.
        Abre o restaurante e retorna uma mensagem de confirmação.
        """
        if self.open == True:
        # BUG 2: O restaurante nunca é realmente aberto porque self.open estava definido como False.
        #Correção: Alterar self.open = True

            self.number_served = 0 # O número de clientes atendidos é resetado para 0
        # BUG 3: O valor self.number_served = -2 não faz sentido, já que o nº de clientes não pode ser negativo.
        # Correção: Alterar self.number_served para 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """
        Fecha o restaurante e retorna uma mensagem de confirmação.
        Se o restaurante já estiver fechado, retorna uma mensagem apropriada.
        """
        if self.open:
            self.open = False
        # REFATORAÇÃO 2: A variável "self.number_served" não é utilizada no metodo.
        # Alteração: Foi adicionada condicional para verificar o recebimento desses valores.
            return f"{self.restaurant_name} agora está fechado!"  # Retorna a mensagem de fechamento
        else:
            return f"{self.restaurant_name} já está fechado!"  # Caso já esteja fechado, retorna essa mensagem

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""

        if not isinstance(total_customers, int) or total_customers < 0:
            return f"Quantidade de cliente não pode ser negativo e precisa ser um valor inteiro!"
        # REFATORAÇÃO 3: O metodo não verificava recebimento de valore menor que zero e não faz sentido um restaurante com cliente negativo.
        # Alteração: Foi adicionada condicional para verificar o recebimento desses valores.
        if self.open:
            self.number_served = total_customers
            return f"A quantidade de cliente é de: {self.number_served}"
        # REFATORAÇÃO 4: Não existia nenhum retorno para quando o número de cliente fosse apresentado.
        # Alteração: Foi adicionado retorno com apresentação da quantidade de cliente.
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""

        if not isinstance(more_customers, int) or more_customers < 0:
            return f"Quantidade de cliente não pode ser negativo e precisa ser um valor inteiro!"
        # REFATORAÇÃO 5: O metodo não verificava recebimento de valores menor que zero e diferente de inteiro.
        # Alteração: Foi adicionada condicional para verificar o recebimento desses valores.

        if self.open:
            self.number_served += more_customers
            return f"O novo número total de cliente é: {self.number_served}"
        #BUG 4: A parte self.number_served = more_customers foi substituída por self.number_served += more_customers, para que o número de cliente seja incrementado corretamente.

        else:
            return f"{self.restaurant_name} está fechado!"



