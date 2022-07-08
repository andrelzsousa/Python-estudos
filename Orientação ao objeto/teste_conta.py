def cria_conta(numero, nome, saldo):
    conta = {'numero': numero, 'nome': nome, 'saldo': saldo }
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(conta['saldo'])



conta = cria_conta(5531, 'andre', 100.32)

deposita(conta, 20)

saca(conta, 100)

extrato(conta)

