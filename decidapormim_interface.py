# Projeto 5 - Decida por mim
# Faça uma pergunta para o programa e ele terá que te dar um resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.resposta = [
            'Concordo',
            'Muito top',
            'Não curto muito a ideia',
            'Faz isso não!'
        ]

    def Inicar(self):
        # layout
        self.layout = [
            [sg.Text('Faça sua pergunta:', size=15), sg.Input(size=30)],
            [sg.Button('Me ajude!', size=45)],
            [sg.Output(size=(50,5))]
        ]
        # janela
        self.janela = sg.Window('Decida Por Mim', layout=self.layout)

        # receber os dados
        while True:
            self.evento, self.valores = self.janela.Read()
            # processar os dados
            if self.evento == 'Me ajude!':
                self.EscolhaDeResposta()

    def EscolhaDeResposta(self):
        self.resposta_final = random.choice(self.resposta)
        print(self.resposta_final)

start = DecidaPorMim()
start.Inicar()
