from tkinter import *
from math import *
import sys

class Aplicacao:

    #Criar o construtor para inicializar a classe

    def __init__(self, janela):
        #Janela
        janela.title('Calculadora Simples')
        janela.geometry('250x300')

        #Espaçamento
        self.frame1 = Frame(janela)
        self.frame1.pack()
        self.frame2 = Frame(janela)
        self.frame2.pack()
        self.frame3 = Frame(janela)
        self.frame3.pack()

        #Operações
        self.frame4 = Frame(janela, pady= 12)
        self.frame4.pack()

        #Resultados
        self.frame5 = Frame(janela)
        self.frame5.pack()

        #Botões
        self.frame6 = Frame(janela, pady= 12)
        self.frame6.pack()

        #Cor e tamanho das letras
        fonte01 = ('verdana', '10')
        Label(self.frame1, text= '', fg= 'black', font= fonte01, height= 1).pack()

        #Botão somar
        btn_somar = Button(self.frame4, font= fonte01, text= ' + ', command= self.somar)
        btn_somar.pack(side= LEFT)

        #Botão subtrair
        btn_subtrair = Button(self.frame4, font=fonte01, text=' - ', command=self.subtrair)
        btn_subtrair.pack(side=LEFT)

        #Botão multiplicar
        btn_multiplicar = Button(self.frame4, font=fonte01, text=' * ', command=self.multiplicar)
        btn_multiplicar.pack(side=LEFT)

        #Botão dividir
        btn_dividir = Button(self.frame4, font=fonte01, text=' / ', command=self.dividir)
        btn_dividir.pack(side=LEFT)

        #Botão raiz quadrada
        btn_raizquadrada = Button(self.frame4, font=fonte01, text=' SQRT', command=self.raizquadrada)
        btn_raizquadrada.pack(side=LEFT)

        #Botão Potenciação
        btn_potenciacao = Button(self.frame4, font=fonte01, text= 'Potência', command=self.potenciacao)
        btn_potenciacao.pack(side=LEFT)

        #Botão sair
        btn_sair = Button(self.frame6, font= fonte01, text= 'Sair', command= self.sair)
        btn_sair.pack(side= LEFT)

        #Entrada de dados
        Label(self.frame2, text= 'Valor 1: ', font= fonte01, width= 8).pack()
        self.valor1 = Entry(self.frame2, width= 10, font= fonte01)
        self.valor1.focus_force()
        self.valor1.pack(side= LEFT)

        Label(self.frame3, text= 'Valor 2: ', font= fonte01, width= 8).pack()
        self.valor2 = Entry(self.frame3, width= 10, font= fonte01)
        self.valor2.pack(side= LEFT)

        #Resultados
        Label(self.frame5, text= ' = ', font= fonte01, width= 8).pack()
        self.msg = Label(self.frame5, width= 10, font= fonte01)
        self.msg.pack(side= LEFT)
        
    def somar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        res = valor1 + valor2
        res = float(res)
        self.msg['text'] = '%.f' % (res)

    def subtrair(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        res = valor1 - valor2
        res = float(res)
        self.msg['text'] = '%.f' % (res)

    def multiplicar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        res = valor1 * valor2
        res = float(res)
        self.msg['text'] = '%.f' % (res)

    def dividir(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        res = valor1 / valor2
        res = float(res)
        self.msg['text'] = '%.2f' % (res)

    def raizquadrada(self):
       try:
           valor1 = self.valor1.get()
           valor1 = float(valor1)
           res = sqrt(valor1)
           self.msg['text'] = '%.2f' % (res)

       except:
           valor2 = self.valor2.get()
           valor2 = float(valor2)
           res = sqrt(valor2)
           self.msg['text'] = '%.2f' % (res)

    def potenciacao(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        res = (valor1**valor2)
        res = float(res)
        self.msg['text'] = '%.f' % (res)

    def sair(self):
        app.destroy()

app = Tk()
Aplicacao(app)
app.mainloop()



