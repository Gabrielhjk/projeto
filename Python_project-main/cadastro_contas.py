import random

def criar_conta(lista_de_contas, cliente):
    tipo_conta = input('Insira o tipo da conta (CORRENTE ou POUPANÇA): ').upper()
    numero_conta = random.randint(1000000, 9999999)
    saldo_inicial = float(input('Insira o valor do depósito inicial: '))

    conta = {
        'tipo': tipo_conta,
        'numero': numero_conta,
        'saldo': saldo_inicial
    }

    lista_de_contas.append(conta)
    print(f'Conta {numero_conta} criada para o cliente {cliente["nome"]}. Saldo inicial: R${saldo_inicial}.')

def realizar_deposito(lista_de_contas, numero_conta, valor):
    for conta in lista_de_contas:
        if conta['numero'] == numero_conta:
            conta['saldo'] += valor
            print(f'Depósito de R${valor} realizado com sucesso na conta {numero_conta}. Novo saldo: R${conta["saldo"]}.')
            return
    print(f'Conta {numero_conta} não encontrada.')

def realizar_saque(lista_de_contas, numero_conta, valor):
    for conta in lista_de_contas:
        if conta['numero'] == numero_conta:
            if conta['saldo'] >= valor:
                conta['saldo'] -= valor
                print(f'Saque de R${valor} realizado com sucesso na conta {numero_conta}. Novo saldo: R${conta["saldo"]}.')
            else:
                print('Saldo insuficiente para realizar o saque.')
            return
    print(f'Conta {numero_conta} não encontrada.')

def realizar_transferencia(lista_de_contas, conta_origem, conta_destino, valor):
    for conta in lista_de_contas:
        if conta['numero'] == conta_origem:
            if conta['saldo'] >= valor:
                for destinatario in lista_de_contas:
                    if destinatario['numero'] == conta_destino:
                        conta['saldo'] -= valor
                        destinatario['saldo'] += valor
                        print(f'Transferência de R${valor} realizada com sucesso da conta {conta_origem} para a conta {conta_destino}.')
                        print(f'Novo saldo da conta {conta_origem}: R${conta["saldo"]}.')
                        print(f'Novo saldo da conta {conta_destino}: R${destinatario["saldo"]}.')
                        return
                print(f'Conta destinatária {conta_destino} não encontrada.')
            else:
                print('Saldo insuficiente para realizar a transferência.')
            return
    print(f'Conta origem {conta_origem} não encontrada.')

def mostrar_saldo(lista_de_contas, numero_conta):
    for conta in lista_de_contas:
        if conta['numero'] == numero_conta:
            print(f'Saldo da conta {numero_conta}: R${conta["saldo"]}.')
            return
    print(f'Conta {numero_conta} não encontrada.')


