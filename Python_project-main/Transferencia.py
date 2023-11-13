
class deposito:
    def __init__(self, saldo):
        while True:
            try:
                self.dep = float(input("Quanto deseja depositar? "))
                if self.dep > 0:
                    self.novo_valor = self.dep
                    break
                else:
                    self.ver = str(input('O depósito deve ser maior que zero.\nDeseja tentar novamente? ')).upper()
                    if self.ver in ['N', 'NÃO', 'NAO']:
                        break
            except ValueError:
                print('Insira algo válido.')

valor = deposito('novo_valor')
valor.novo_valor

class saque:
    def __init__(self, saqu):
        while True:
            try:
                self.saqu = input("Deseja sacar algum valor? ").upper()
                if self.saqu in ["S", "SIM"]:
                    self.retiro_saqu = int(input("Quanto deseja sacar? "))
                    if self.retiro_saqu < deposito('novo_valor'):
                        self.res = self.retiro_saqu - deposito('novo_valor')
                        print('Saque realizado :)')
                        break
                    else:
                        print(f'O valor do saque não pode ser maior que seu saldo atual.\n Saldo atual: {valor}')
                else:
                    print("Obrigado pela visita!")
                    break
            except ValueError:
                print('Insira algo válido.')
sak = saque('retiro_saqu')
sak.res


class transferencia:
    def __init__(self, transf):
        while True:
            try:
                self.transf = input("Deseja fazer uma transferencia? ").upper()
                if self.transf in ["S", "SIM"]:
                    #método for
                    self.pessoa_tran = input("Pra quem deseja fazer a transferencia? ")
                    self.saldo_tran = int(input("Quanto deseja transferir? "))
                    if self.saldo_tran < #saldo:
                        #destino é vazio
                        #para conta na lista_de_contas:
                        #se o numero da conta for igual a self.pessoa_tran
                        #destino é
                        print("Valor transferido!")
                        #break
                    else:
                        print('Insira valor maior que Zero')
                elif self.transf in ['N', 'NÃO', 'NAO']:
                    print("Obrigado pela visita!")
            except ValueError:
                print('Insira valores válidos.')

# tr = transferencia('saldo_tran')
# tr.saldo_tran

class verificar_saldo:
    def __init__(self, verific):
        verificar_saldo = True
        self.verificacao = input("Deseja vereficar saldo da conta? ")
        if self.verificacao in ['SIM', 'S']:
            verificar_saldo = False
        else:
            print("Obrigado pela visita!")

class historico:
    def __init__(self):
        pass
