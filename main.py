menu = '''
[d] deposito
[s] saque
[e] saldo
[q] sair
'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(f"{menu} digite uma opcao: ")
    
    if opcao =='d':
        deposito = float(input("deposite o valor: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"depositou: R$ {deposito}\n"
            
        else:
            print('não foi possivel fazer esse transferencia')
        
    elif opcao == 's':
        
        if numero_saques >= LIMITE_SAQUES:
            print('não é mais possível sacar hoje')
            break
            
        saque=float(input('informe o valor do saque: '))
            
        if saldo >= saque:
            print(f'foi sacado R${saque}')
            extrato += f"sacou R$ {saque}"
            numero_saques += 1
            saldo -= saque
        
        else:
            print('não foi possivel fazer esse transferencia')
        
    elif opcao == 'e':
        print("nao foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSando: R${saldo}")
        
    elif opcao == 'q':
        print('saindo')
        break
    else:
        print("opção invalida")
