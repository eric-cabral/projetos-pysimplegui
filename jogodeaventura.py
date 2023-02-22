# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar vários finais
# diferentes baseados nas respostas que forem dadas

# Eu quero chegar a finais diferentes na minha história,
# de acordo com as respostas que eu passe ao programa

# Qual é o cenário: Eu estou numa guerra entre duas nações,
# e nós temos 2 lados: LadoA e LadoB. Somente o LadoA irá
# vencer então eu tenho que tomar as decisões corretas
# para chegar até a vitória, que somente o LadoA irá conseguir!

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
        resposta1 = input(self.pergunta1)
        if resposta1.title() == 'Norte':
            resposta1B = input(self.pergunta2)
            if resposta1B.title() == 'Espada':
                print(self.final1)
            if resposta1B.title() == 'Escudo':
                print(self.final2)
        if resposta1 == 'Sul':
            resposta1B = input(self.pergunta3)
            if resposta1B.title() == 'Linha de frente':
                print(self.final3)
            if resposta1B.title() == 'Tático':
                print(self.final4)

jogo = JogoDeAventura()
jogo.Iniciar()
