# Projeto 3 - Chute o número
# Objetivo - Criar um algoritmo que gera um valor aleatório
# e eu tenho que ficar tentando o número até eu acertar
import random

class ChuteONumero:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 100
        # layout
        # janela
        # extrair os dados

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
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
