import random


class Conta:

    def __init__(self, limite=1000.00):
        
        #print('Contruindo objeto... {}'.format(self))

        self.__numero = random.randrange(1000,10000)

        self.__titular = input('Qual o seu nome? ').title()

        self.__saldo = float(input('Deposite o valor que deseja na conta: '))

        self.__limite = limite

        print('---------------------------------------------------------------------------------------------------')
        print('Sua conta foi criada, {}'.format(self.__titular))
        print('Bem vindo ao DecoBank!')
        print('As funções possíveis são: saca(valor), deposita(valor), transfere(valor, conta), extrato(), info()')
        print('---------------------------------------------------------------------------------------------------')
         
      
    #operações/métodos com o saldo da conta

    def deposita(self, valor):
        self.__saldo += valor
        print('-----------------------------------------------------------')
        print('Você depositou {} reais na sua conta.'.format(valor))
        print('-----------------------------------------------------------')


    def saca(self, valor):
        
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print('-----------------------------------------------------------')
            print('Você sacou {} reais da sua conta.'.format(valor))
            print('-----------------------------------------------------------')
            
        else:    
            print('-----------------------------------------------------------')
            print('Não há fundos suficientes na sua conta para realizar esse saque.')
            print('-----------------------------------------------------------')
    
    def transfere(self, valor, conta):

        if(self.__pode_sacar(valor)):

            self.__saldo = self.__saldo - valor
            conta.__saldo += valor
            print('-----------------------------------------------------------')
            print('Você transferiu R$ {} para a conta de {}'.format(valor, conta.__titular))
            print('-----------------------------------------------------------')
            
        else: 
            print('-----------------------------------------------------------')
            print('Não há fundos suficientes na sua conta para realizar essa transferência.')
            print('-----------------------------------------------------------')


    #operações/métodos com informações sobre a conta 
      
    def info(self):
        print('-----------------------------------------------------------')
        print('Nome do titular: {}'.format(self.__titular))
        print('Número da conta: {}'.format(self.__numero))
        print('O limite de crédito da sua conta é de R$ {}'.format(self.__limite))
        print('-----------------------------------------------------------')

    def extrato (self):
        print('-----------------------------------------------------------')
        print('{}, seu saldo é de R$ {}'.format(self.__titular, self.__saldo))
        print('-----------------------------------------------------------')

    
    #getters

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite


    #setters

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite


    #métodos privados

    def __pode_sacar(self, valor):

        valor_disponivel_para_saque = self.__saldo + self.__limite
        return  valor <= valor_disponivel_para_saque

    
    #métodos estáticos

    @staticmethod
    def codigo_do_banco():
        codigo_decobank = '011'
        return codigo_decobank




#from conta import Conta



