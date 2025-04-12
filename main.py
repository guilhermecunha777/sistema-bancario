import textwrap

# Constantes e variáveis
AGENCIA = "0001"
LIMITE_SAQUES = 3

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
usuarios = []
contas = []

def menu():
    menu = '''\n
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair
    [c] Criar usuário
    [nc] Criar nova conta
    [l] Listar usuários
    '''
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print('Não foi possível realizar essa operação.')
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print('Não é mais possível sacar hoje.')
    elif valor > limite:
        print('Valor excede o limite por saque.')
    elif valor > saldo:
        print('Saldo insuficiente.')
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f'Você sacou R$ {valor:.2f}')
    else:
        print('Valor inválido.')

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n========= EXTRATO =========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o seu nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

    print("Usuário não encontrado, criação de conta encerrada!")

# Loop principal
while True:
    opcao = menu()

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES,
        )

    elif opcao == 'e':
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'q':
        break

    elif opcao == 'c':
        criar_usuario(usuarios)

    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == 'l':
        for usuario in usuarios:
            print(usuario)

    else:
        print("Opção inválida.")
