contas = [{
    'nome': 'Eliseu',
    'cpf_cnpj': '123.123.123-12',
    'tipo_conta': 'p',
    'saldo': 500,
    'senha': 123456
},{
    'nome': 'Elias',
    'cpf_cnpj': '12.123.123/0001-12',
    'tipo_conta': 'j',
    'saldo': 300,
    'senha': 123457
}]

opcao = 0

def login():

    tipo = input('Informe o tipo de conta: ')
    print('C: corrente, P: poupança, S: salário, J: jurídica')

    if tipo == 'j' or 'J':
        login = int(input('Informe o CNPJ, apenas números: '))
    else:
        login = int(input('Informe seu CPF, apenas números: '))

    for conta in contas:

        if conta['cpf_cnpj']  == login:
            
            contador = 3

            senha = int(input(f"Olá {conta['nome']}, informe sua senha: "))


            while contador != 1:

                contador -= 1

                if conta['senha'] == senha:
                    print('Login realizado com sucesso!')
                    return conta 
                else:
                    senha = int(input(f"Senha incorreta! Tente novamente. Lembrando, você só tem {contador} chances. "))

def transferir(conta):

    conta_destino = int(input('Digite o cpf ou cnpj da conta destino: '))
    vlr = float(input('Digite o valor que você quer transferir: '))

    for destino in contas:
        if conta_destino == destino['cpf_cnpj']:
            conta['saldo'] -= vlr
            destino['saldo'] += vlr
        
    print("__________Tranzação realizada com sucesso!_________")
    print(f"Origem: {conta['nome']} CPF: {conta['cpf_cnpj']}  Saldo: {conta['saldo']}")
    print(f"Destino: {destino['nome']} CPF: {destino['cpf_cnpj']}  Saldo: {destino['saldo']}")

                
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
                vlr = float(input(f"{conta['nome']}, digite o valor do deposito: "))
                depositar(vlr, conta)
                print(conta)

            elif opcao == 2:
                print('Transferir')
                transferir(conta)

    elif opcao == 3:
        print(contas)
    else:
        print('Opção incorreta.')