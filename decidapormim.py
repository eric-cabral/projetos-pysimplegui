# Projeto 5 - Decida por mim
# Faça uma pergunta para o programa e ele terá que te dar um resposta
import random

class DecidaPorMim:
    def __init__(self):
        self.resposta = [
            'Concordo',
            'Muito top',
            'Não curto muito a ideia',
            'Faz isso não!'
        ]

    def Inicar(self):
        self.pergunta = input('Qual a sua dúvida?\n P: ')
        self.EscolhaDeResposta()

    def EscolhaDeResposta(self):
        self.resposta_final = random.choice(self.resposta)
        print(self.resposta_final)

start = DecidaPorMim()
start.Inicar()
