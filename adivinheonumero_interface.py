# Projeto 3 - Chute o número
# Objetivo - Criar um algoritmo que gera um valor aleatório
# e eu tenho que ficar tentando o número até eu acertar
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 100

    def Iniciar(self):
        # layout
        self.layout = [
            [sg.Text('SEU CHUTE', size=(20, 0))],
            [sg.Input(size=(20, 0), key='ValorChute'), sg.Button('Chute!')],
            [sg.Output(size=(26, 2))]
        ]
        # janela
        self.janela = sg.Window('ADIVINHE O NÚMERO - INTERFACE', layout=self.layout)

        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while True:
                # receber os dados
                self.evento, self.valores = self.janela.Read()
                # fazer algo com os dados
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while True:
                        if chute > self.sorteado:
                            print('Chute um valor mais baixo!')
                        elif chute < self.sorteado:
                            print('Chute um valor mais alto!')
                        else:
                            print('PARABÉNS, você acertou o chute!!!')
                            break
        except:
            print('Por favor digite apenas números!')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.chute = int(input('Chute um número: '))

    def GerarNumeroAleatorio(self):
        self.sorteado = random.randint(self.valor_minimo, self.valor_maximo)


start = ChuteONumero()
start.Iniciar()
