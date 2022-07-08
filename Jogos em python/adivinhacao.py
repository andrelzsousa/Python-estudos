import random
import jogos

def jogar():
    print('------------------------------------------------------')
    print("Bem vindo ao jogo de adivinhação!")
    print('------------------------------------------------------')
    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    while(True):

        print('Escolha o nível de dificuldade')
        print('(1) Fácil  (2) Médio  (3) difícil')

        nivel = int(input(' ')) 

        if(nivel == 1):
            tentativas = 12
            break
        elif(nivel == 2):
            tentativas = 8
            break
        elif(nivel == 3):
            tentativas = 3
            break
        else:
            print('Por favor, digite 1, 2 ou 3.')


    for rodada in range(1, tentativas + 1):
        print('------------------------------------------------------')
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute>100):
            print('Você deve digitar um número entre 1 e 100!')
            continue 
        

        acertou = chute == numero_secreto 
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('------------------------------------------------------')
            print('Você acertou! {} é o número secreto. Você fez {} pontos!'.format(numero_secreto, pontos))
            print('------------------------------------------------------')
            break
        else: 
            if(maior):
                print('Você errou! {} é maior que o número secreto.'.format(chute))
            if(menor):
                print('Você errou! {} é menor que o número secreto.'.format(chute))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    if(rodada == tentativas):
        print('------------------------------------------------------')
        print('Fim do jogo. O número secreto era {}'.format(numero_secreto))
        print('------------------------------------------------------')
    else:
        print('Fim do jogo.')

    fim = int(input('(1) Jogar novamente  (2) Voltar ao menu  (3) Sair '))

    if(fim == 1):
        jogar()
    elif(fim == 2):
        jogos.escolhe_jogo()
    elif(fim == 3):
        print('xau!')

if(__name__ == "__main__"):
    jogar()
