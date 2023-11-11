
class deposito:
    def __init__(self, saldo):
        self.saldo = "0R$"
        print(f"Seu saldo atual é {self.saldo}")
        self.dep = int(input("Quanto deseja depositar? "))
        if self.dep > 0:
            pass
        else:
            print("Não é possível depositar esse valor, Tente novamente!")
            self.dep = int(input("Quanto deseja depositar? "))

        self.novo_valor = self.dep
        print(f"Seu saldo atual é {self.novo_valor}R$")

valor = deposito('novo_valor')
valor.novo_valor

class saque:
    def __init__(self, saqu):
        self.saqu = True
        self.saqu = input("Deseja sacar algum valor? ").upper()
        if self.saqu in ["S", "SIM"]:
            self.saqu = False
        else:
            print("Obrigado pela visita!")

        print(f"Saldo suficiente {valor}")
        self.retiro_saqu = int(input("Quanto deseja sacar? "))
        while True:
            if self.retiro_saqu < 0:
                print("Não é possivel sacar esse valor")
            else:
                print("Retirado com sucesso!")
            break

sak = saque('retiro_saqu')
sak.retiro_saqu

class transferencia:
    def __init__(self, transf):
        transferencia = True
        self.transf = input("Deseja fazer uma transferencia? ").upper()
        if self.transf in ["S", "SIM"]:
            transferencia = False
        else:
            print("Obrigado pela visita!")

        self.pessoa_tran = input("Pra quem deseja fazer a transferencia? ")
        self.saldo_tran = int(input("Quanto deseja transferir? "))
        if self.saldo_tran < 0:
            print("Valor indisponível")
        else:
            print(f"Tranferência feita com sucesso, Você transferiu {self.saldo_tran}R$ para {self.pessoa_tran}!")

tr = transferencia('saldo_tran')
tr.saldo_tran

class verificar_saldo:
    def __init__(self, verific):
        verificar_saldo = True
        self.verificacao = input("Deseja vereficar saldo da conta? ")
        if self.verificacao in ['SIM', 'S']:
            verificar_saldo = False
        else:
            print("Obrigado pela visita!")

        print(valor - sak)
        return valor - sal_trs

verific = verificar_saldo('verficacao')
verific.verificacao
valor.novo_valor
sak.retiro_saqu
tr.saldo_tran

class historico:
    def __init__(self):
        return valor, sak, tr
