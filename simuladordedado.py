from random import randint
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de um valor para o dado virtual? '
        # layout
        self.layout = [
            [sg.Text('Jogar o dado?', size=15)],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        # janela
        self.janela = sg.Window('Simulador de Dado',  layout=self.layout)
        # ler os valor da tela
        self.resposta, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.resposta == 'Sim' or self.resposta == 's':
                self.GerarValorDoDado()
            elif self.resposta == 'Não' or self.resposta == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Digite uma resposta correta, por favor!')
        except:
            print('Ocorreu um erro ao receber sua resposta')


    def GerarValorDoDado(self):
        print(randint(self.valor_minimo, self.valor_maximo))

# Programa Principal
simulador = SimuladorDeDado()
simulador.Iniciar()
