import random
import jogos


def jogar():

    mensagem_inicio()

    print('Tema: (1) LoL  (2) Frutas  (3) Academia')
    tema = int(input('Qual tema você deseja jogar? '))

    if(tema == 1):
        palavra_secreta = gera_palavra_secreta("champions.txt")
    if(tema == 2):
        palavra_secreta = gera_palavra_secreta("frutas.txt")
    if(tema == 3):
        palavra_secreta = gera_palavra_secreta("academia.txt")

    letras_acertadas = []
    letras_erradas = []

    for letra in palavra_secreta:
        if letra != " ":
            letras_acertadas.append("_")
        else:
            letras_acertadas.append(" ")

    tentativas = 5

    while(True):

        print('------------------------------------------------------')
        print('Você tem {} tentativas.'.format(tentativas))
        print('letras erradas:', *letras_erradas, sep=' ')
        print('Qual a letra?', *letras_acertadas, sep=' ')
        chute = input(" ")

        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas -= 1
            letras_erradas.append(chute)

        # fim de jogo (vitoria ou derrota)
        if(tentativas == 0):
            print(" ")
            print('Suas tentativas acabaram. Você foi enforcado.')
            print('A palavra era {}'.format(palavra_secreta))
            imprime_desenho_perdedor()
            break

        if("_" not in letras_acertadas):
            print(palavra_secreta)
            print('Parabéns! Você acertou a palavra.')
            imprime_desenho_vencedor()
            break

        if(palavra_secreta.upper() == chute.upper()):
            print(palavra_secreta)
            print('Parabéns! Você acertou a palavra.')
            imprime_desenho_vencedor()
            break

    fim = int(input('(1) Jogar novamente  (2) Voltar ao menu  (3) Sair '))

    if(fim == 1):
        jogar()
    elif(fim == 2):
        jogos.escolhe_jogo()
    elif(fim == 3):
        print('xau!')


def mensagem_inicio():
    print('------------------------------------------------------')
    print("Bem vindo ao jogo de forca!   ")


def gera_palavra_secreta(nome_do_arquivo):
    arquivo = open(nome_do_arquivo, "r")

    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()
    arquivo.close()


def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:

        if(letra.upper() == chute.upper()):
            letras_acertadas[index] = letra

        index = index + 1

def imprime_desenho_perdedor():

    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('------------------------------------------------------')


def imprime_desenho_vencedor():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print('------------------------------------------------------')


if(__name__ == "__main__"):
    jogar()
