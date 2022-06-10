class bombaCombustivel():
    def _init_(self):
        self.tipoCombustivel = 'Comum'
        self.valorLitro = 9.00
        self.quantidadeCombustivel = 40000

    def abastecerPorValor(self):
        valor = float(input('Qual o valor em dinheiro que você quer de gasolina?: '))

        if self.quantidadeCombustivel < (valor / self.valorLitro):
            print('Não há combustível suficiente para o abastecimento')
            return
        else:
            valorTiradoDaBomba = valor / self.valorLitro
            self.quantidadeCombustivel -= valorTiradoDaBomba

        print('Obrigado por abastecer conosco, a quantidade de litros foi: ', valorTiradoDaBomba, 'de gasolina',
              self.tipoCombustivel)

    def abastecerPorLitro(self):
        valor = float(input('Qual o valor em litros que você deseja de gasolina?: '))

        if self.quantidadeCombustivel < valor:
            print('Não há combustível suficiente para o abastecimento')
        else:
            valorTiradoDaBomba = valor
            self.quantidadeCombustivel -= valorTiradoDaBomba
            valorASerPago = valor * self.valorLitro

        print('Por favor, pague R$', valorASerPago, 'de gasolina', self.tipoCombustivel)

    def alterarValor(self):
        valor = float(input('Qual o preço que você deseja?: '))
        if valor == 0:
            print('O valor não pode ser 0')
            return
        self.valorLitro = valor

    def alterarCombustivel(self):
        valor = input('Qual o tipo de gasolina que você deseja?: ')
        self.tipoCombustivel = valor

    def alterarQuantidadeCombustivel(self):
        valor = float(input('Qual a quantidade de litros na bomba que você deseja?: '))
        self.quantidadeCombustivel = valor


def main():
    Carro = bombaCombustivel()

    opc = None

    while opc != "0":
        print(
            """
            Bem-vindo ao posto, o que deseja?
    
            1 - Abasteça o carro por um valor em dinheiro
            2 - Abasteça o carro por um valor em litros
            3 - Altere o valor do Combustível
            4 - Altere o tipo do Combustível
            5 - Altere a quantidade do Combustível na bomba
            0 - Sair
    
            """
        )

        opc = input('Opção: ')

        if opc == "0":
            print('Obrigado por abastecer conosco')
        elif opc == "1":
            Carro.abastecerPorValor()
        elif opc == "2":
            Carro.abastecerPorLitro()
        elif opc == "3":
            Carro.alterarValor()
        elif opc == "4":
            Carro.alterarCombustivel()
        elif opc == "5":
            Carro.alterarQuantidadeCombustivel()
        else:
            print('Função inválida!')


main()