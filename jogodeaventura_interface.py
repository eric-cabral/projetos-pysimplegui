# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar vários finais
# diferentes baseados nas respostas que forem dadas

# Eu quero chegar a finais diferentes na minha história,
# de acordo com as respostas que eu passe ao programa

# Qual é o cenário: Eu estou numa guerra entre duas nações,
# e nós temos 2 lados: LadoA e LadoB. Somente o LadoA irá
# vencer então eu tenho que tomar as decisões corretas
# para chegar até a vitória, que somente o LadoA irá conseguir!
import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        # LadoA = Norte | LadoB = Sul
        self.pergunta1 = 'Onde você nasceu (Norte ou Sul)? '
        # LadoA = Espada | LadoB = Escudo
        self.pergunta2 = 'Espada ou escudo? '
        # LadoA = Linha de frente | LadoB = Tático
        self.pergunta3 = 'Especialidade (Linha de frente/Tático)? '
        # Finais da história
        self.final1 = 'Você será um herói na linha de frente!'
        self.final2 = 'Você será um herói protegendo todas as nossas tropas!'
        self.final3 = 'Você irá sacrificar na batalha!'
        self.final4 = 'Você não é capaz de lutar nessa batalha!'

    def Iniciar(self):
        # layout
        self.layout = [
            [sg.Output(size=(30,2),key='respostas')],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('INICIAR'), sg.Button('RESPONDER')]
        ]
        # janela
        self.janela = sg.Window('Jogo De Aventura', layout=self.layout)

        while True:
            # ler os dados
            self.LerValores()
            # utilizar os dados
            if self.evento == 'INICIAR':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'Norte':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'Espada':
                        print(self.final1)
                    if self.valores['escolha'] == 'Escudo':
                        print(self.final2)
                if self.valores['escolha'] == 'Sul':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'Linha de frente':
                        print(self.final3)
                    if self.valores['escolha'] == 'Tático':
                        print(self.final4)

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()
