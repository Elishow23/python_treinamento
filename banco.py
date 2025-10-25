contas = [{
    'nome': 'Eliseu',
    'cpf_cnpj': 1212,
    'tipo_conta': 'p',
    'saldo': 150,
    'senha': 123456
},{
    'nome': 'Elias',
    'cpf_cnpj': 1313,
    'tipo_conta': 'j',
    'saldo': 200,
    'senha': 123457
}]

opcao = 0

def login():

    login = int(input('Informe seu CPF ou CNPJ: '))

    for conta in contas:
        if conta['cpf_cnpj']  == login:
            
            contador = 3

            senha = int(input(f'Olá {conta['nome']}, informe sua senha: '))


            while contador != 1:
                

                contador -= 1

                if conta['senha'] == senha:
                    print('Login realizado com sucesso!')
                    return conta 
                else:
                    senha = int(input(f'Senha incorreta! Tente novamente. Lembrando, você só tem {contador} chances. '))
        else:
            print('Essa conta não existe no nosso banco de dados. Realize seu cadastro.')
            nome = input('Nome: ')
            cpf = int(input('CPF ou CNPJ: '))
            tipo = input('Tipo de conta: ')
            senha= int(input('Defina sua senha: '))
            cadastro(nome, cpf, tipo, senha)
            break

def transferir(conta_origem, conta_destino, vlr):

        for conta in contas:
              if conta_destino == conta:
                print(conta)
                print(conta_origem)
                print(vlr)
        
        '''print(f'Saldo de {conta_origem['nome']} é: {conta_origem['saldo']}')
        print(f'Saldo de {conta['nome']} é: {conta['saldo']}')
        print('Transferencia realizada com sucesso!')'''
                
def depositar(vlr, conta):

    conta['saldo'] += vlr

def cadastro(nome, cpf, tipo, senha):

    conta = {
        'nome': nome,
        'cpf_cnpj': cpf,
        'tipo_conta': tipo,
        'saldo': 0,
        'senha': senha
    }

    contas.append(conta)

    print('Cadastro realizado com sucesso!')

    print(contas)
        

while True:

    print('________Sistema Bancário________')
    print('1: Fazer login')
    print('0: Sair')

    opcao = int(input())


    if opcao == 0:
        print('Você saiu do sistema bancario!')
        break
    elif opcao == 1:
        print('_________login_________')
        conta = login()

        opcao = 0

        while True:

            print('1: Depositar')
            print('2: Transferir')
            print('0: Sair')
            opcao = int(input('Escolha uma das opcões: '))

            if opcao == 0:
                print('Você saiu da conta.')
                break

            elif opcao == 1:
                print('__________Depositar__________')
                vlr = float(input(f'{conta['nome']}, digite o valor do deposito: '))
                depositar(vlr, conta)
                print(conta)

            elif opcao == 2:
                print('Transferir')
                conta_destino = int(input('Digite o cpf ou cnpj da conta destino: '))
                vlr = float(input('Digite o valor que você quer transferir: '))
                conta_origem = conta
                transferir(conta_origem, conta_destino, vlr)

    elif opcao == 3:
        print(contas)
    else:
        print('Opção incorreta.')