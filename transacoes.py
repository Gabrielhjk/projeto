from cadastro_de_cliente import, cliente
from cadastro_contas import, conta

class deposito:
    def __init__(self, saldo):
        self.saldo = 0
        print(f"Seu saldo atual é {self.saldo}")

    def colocar_saldo(self, dep):
        dep = input("Quanto deseja depositar? ")

    def depositado(self, novo_valor):
        novo_valor = self.dep
        print(f"Seu saldo atual é {novo_valor}")

class saque:
    def __init__(self):
        self.saque = input("deseja sacar? ").upper()
        if self.saque in ["S", "SIM"]:
          saque = False

    def retiro_saque(self):
        print(f"Saldo suficiente {(deposito.depositado(novo_valor=int))}")
        self.retiro_saque = input("Quanto deseja sacar? ")
        if self.retiro_saque <= 0:
            print("Não é possivel sacar esse valor")
        else:
            print("Retirado com sucesso!")

        b = deposito.depositado(novo_valor=int)
        return b - self.retiro_saque

class transferencia:
    def __init__(self, transf, pessoa_tran):
        self.transf = input("deseja fazer uma transferencia? ").upper()
        if self.transf in ["S", "SIM"]:
          transferencia = False

        self.pessoa_tran = input("Pra quem deseja fazer a transferencia? ")

    def saldo_transferencia(self, saldo_tran):
        self.saldo_tran = input("Quanto deseja transferir? ")
        if self.saldo_tran <= 0:
            print("Valor indisponível")
        else:
            print("Tranferência feita com sucesso!")

class verificar_saldo:
    def __init__(self):
        self.verificacao = input("Deseja vereficar saldo da conta? ")
        if self.verificacao in ['SIM', 'S']:
            verificar_saldo = False

class historico:
    def __init__(self):
        return transferencia.saldo_transferencia(saldo_tran=int)
