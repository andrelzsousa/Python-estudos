import adivinhacao
import forca

def mensagem():
    print('------------------------------------------------------')
    print(" Bem vindo aos jogos em Python! ")


def escolhe_jogo():

    print('------------------------------------------------------')
    print('(1) adivinhação  (2) forca')
    jogo = int(input('Qual jogo deseja jogar? '))

    if(jogo == 1):
        print('jogando adivinhação')
        adivinhacao.jogar()
        
    elif(jogo == 2):
        print('jogando forca')
        forca.jogar()

if(__name__ == "__main__"):
    mensagem()
    escolhe_jogo()