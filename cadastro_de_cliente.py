cliente = {
    'nome': '',
    'email': '',
    'endereco': '',
    'telefone': '',
    'senha': ''
}

def cadastrando(lista_de_clientes: list):
    client = cliente.copy()
    print('Insira as seguintes credenciais: ')
    client['nome'] = input('Nome: ')
    client['endereco'] = input('Endereço: ')
    client['telefone'] = int(input('Telefone, apenas números: '))
    while True:
        email = input('Email: ')
        if '@' in email:
            client["email"] = email
            break
        else:
            print('O email deve conter "@"')
    for cliente_atual in lista_de_clientes:
        if client["email"] == cliente_atual['email']:
            print('Este email já está cadastrado, efetue login.')
            return
    client['senha'] = input('Crie sua Senha: ')
    lista_de_clientes.append(client)
    print('Cadastro realizado!!\nBoas vindas ao nosso banco :)')
'''
#Falta atribuir

def editar(lista_de_clientes: list):
    email = input('Digite seu email: ')
    for cliente_atual in lista_de_clientes:
        if email == cliente_atual['email']:
            print('Os dados são: ')
            print(cliente_atual['nome'])
            print(cliente_atual['email'])
            print(cliente_atual['endereco'])
            print(cliente_atual['telefone'])
            opcao = input('Deseja alterar esse usuário? (SIM/NÃO): ').upper()
            if opcao == 'SIM' or opcao == 'S':
                cliente_atual['nome'] = input('Insira o novo Nome: ')
                cliente_atual['email'] = input('Insira o novo E-mail: ')
                cliente_atual['endereco'] = input('Insira o novo Endereço: ')
                cliente_atual['telefone'] = input('Insira o novo Telefone: ')
                cliente_atual['senha'] = input('Insira o nova Senha: ')
                print('Atualizado :) ')
                return
            else:
                print('Alteração cancelada!')
                return
    else:
        print('Credencial não encontrada.')
'''

def login(lista_de_clientes):
    while True:
        try:
            email = input('Email: ')
            senha = input('Senha: ')
            for cliente_atual in lista_de_clientes:
                if email == cliente_atual.get('email') and senha == cliente_atual.get('senha'):
                    print('Login Feito')
                    return cliente_atual
            print('Email ou senha incorretos, tente novamente.')
            cad = input('Email não encontrado no banco de dados, deseja realizar cadastro? (S/N): ').upper()
            if cad in ["S", "SIM"]:
                cadastrando(lista_de_clientes)
        except ValueError:
            print('Insira valores válidos!')
