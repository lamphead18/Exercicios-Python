from random import randrange
import sys


class Tamagochi(object):
    maximo_saude = 10
    aviso_saude = 3
    maximo_comida = 10
    aviso_comida = 3
    maximo_idade = 10

    def _init_(self, nome):
        self.nome = nome
        self.comida = randrange(self.maximo_comida)
        self.saude = randrange(self.maximo_saude)
        self.idade = 0

    def __passa_tempo(self):
        self.saude -= 1
        self.comida -= 1
        self.idade += 0.1
        if self.idade > 10:
            print('Seu tamagotchi foi de caixa ;-;')
            sys.exit()

    def felicidade(self):
        if self.comida > self.aviso_comida and self.saude > self.aviso_saude:
            return "Feliz"
        elif self.comida < self.aviso_comida:
            return "Com fome"
        else:
            return "Entediado"

    def _str_(self):
        print("\nMeu nome é" + self.nome + "." "\nStatus:\ncomida: " + str(self.comida) + "\nsaúde: " + str(
            self.saude) + "\nidade: " + str(self.idade) + "\nMe sinto: " + self.felicidade() + ".")

    def alimentar(self):
        valor = int(input('Quanto de comida você quer dar?: '))
        self.comida += valor

        if self.comida < 0:
            self.comida = 0
            print('Ainda estou com fome!')
        elif self.comida > self.maximo_comida:
            self.comida = self.maximo_comida
            print('Estou cheio!')
        self.__passa_tempo()

    def brincar(self):
        print('Adoro brincar :)!')
        valor = int(input('Quanto tempo você quer brincar?: '))
        self.saude += valor

        if self.saude < 0:
            self.saude = 0
            print('Estou entediado :( ...')
        elif self.saude > self.maximo_saude:
            self.saude = self.maximo_saude
            print('Estou feliz!')
        self.__passa_tempo()


def main():
    nome_tamagotchi = input('Qual o nome do seu tamagotchi? ')

    meu_tamagotchi = nome_tamagotchi(nome_tamagotchi)

    input(
        'Olá! Meu nome é ' +
        meu_tamagotchi.nome +
        ' e sou novo por aqui!' +
        '\nPressione enter para começar\n'
    )

    opc = None

    while opc != "0":
        print(
            """
            **INTERAJA COM SEU TAMAGOTCHI**
    
            1 - Alimente
            2 - Brinque
            0 - Sair
    
            """
        )

        opc = input('Opção: ')

        if opc == "0":
            print('Até logo')
        elif opc == "1":
            meu_tamagotchi.alimentar()
        elif opc == "2":
            meu_tamagotchi.brincar()
        elif opc == "Segredo":
            meu_tamagotchi._str_()
        else:
            print('Função inválida!')


main()