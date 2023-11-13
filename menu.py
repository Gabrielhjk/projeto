import os
import cadastro_de_cliente
import cadastro_contas


def menu_inicial():
    os.system('cls')
    print('BOAS-VINDAS AO *BANCO FICTÍCIO*.\nAQUI SEU DINHEIRO RENDE 50% AO DIA.\nESCOLHA UMA OPÇÃO PARA CONTINUAR.')
    print('Digite 1 se você é CLIENTE')
    print('Digite 2 se você é FUNCIONÁRIO')
    print('Digite 0 para encerrar')

if __name__ == '__main__':
    lista_de_clientes = []
    lista_de_contas = []
    sistema = True
    cliente_logado = None

    while sistema:
        menu_inicial()
        try:
            opcao = int(input('Digite o número da opção desejada: '))
            if opcao == 1:
                verificar = int(input('Digite 1 para Cadastrar ou 2 para efetuar Login: '))
                if verificar == 1:
                    cadastro_de_cliente.cadastrando(lista_de_clientes)
                elif verificar == 2:
                    cliente_logado = cadastro_de_cliente.login(lista_de_clientes)
                    if cliente_logado:
                        if 'conta' not in cliente_logado:
                            cadastro_contas.criar_conta(lista_de_contas, cliente_logado)
                            cliente_logado['conta'] = lista_de_contas[-1]['numero']
                            print(f"Conta {cliente_logado['conta']} criada para o cliente {cliente_logado['nome']}.")
                        while True:
                            print('Selecione a operação:')
                            print('1. Depósito')
                            print('2. Saque')
                            print('3. Transferência')
                            print('4. Mostrar Saldo')
                            print('0. Sair')
                            escolha = int(input('Digite o número da opção desejada: '))
                            if escolha == 1:
                                valor_deposito = float(input('Digite o valor do depósito: '))
                                cadastro_contas.realizar_deposito(lista_de_contas, cliente_logado['conta'], valor_deposito)
                            elif escolha == 2:
                                valor_saque = float(input('Digite o valor do saque: '))
                                cadastro_contas.realizar_saque(lista_de_contas, cliente_logado['conta'], valor_saque)
                            elif escolha == 3:
                                numero_destinatario = int(input('Digite o número da conta destinatária: '))
                                destinatario = None
                                for conta in lista_de_contas:
                                    if conta['numero'] == numero_destinatario:
                                        destinatario = conta
                                        break
                                if destinatario:
                                    valor_transferencia = float(input('Digite o valor da transferência: '))
                                    cadastro_contas.realizar_transferencia(lista_de_contas, cliente_logado['conta'], destinatario, valor_transferencia)
                                else:
                                    print('Conta destinatária não encontrada.')
                            elif escolha == 4:
                                cadastro_contas.mostrar_saldo(lista_de_contas, cliente_logado['conta'])
                            elif escolha == 0:
                                break
                            else:
                                print('Opção inválida.')
                    else:
                        print('Login não realizado. Tente novamente.')
                else:
                    print('Opção inválida.')
            elif opcao == 2:
                cadastro_contas.funcionario()
            elif opcao == 0:
                print('Volte sempre!')
                sistema = False
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Valor inválido. Por favor, digite um número.')
