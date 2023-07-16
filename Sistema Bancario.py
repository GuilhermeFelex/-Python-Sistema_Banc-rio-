#set variable
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#layout menu
menu = """
==================== MENU ====================

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    => """

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("\nInsira o valor que deseja depositar: "))
        if deposito > 10:
            saldo += deposito
            extrato += (f"Deposito: R$ {deposito:.2f}\n")
            print (f"O valor de R$ {deposito:.2f} foi deposito com sucesso!")

        else:
            print("Operação Falhou! O Valor informado é inválido. ")
 

    elif opcao == "2":
        saque = float(input("\nInsira o valor que deseja sacar: "))
       
        excedeu_limite = saque > limite

        excedeu_saldo = saque > saldo

        excedeu_saque = numero_saques >= LIMITE_SAQUES
       
        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente. ")

        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite da transação. ")

        elif excedeu_saque:
            print("Operação Falhou! Número máximo de saques diários excedido. ")

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += (f"saque: -R$ {saque:.2f}\n")
            print (f"O valor de R$ {saque:.2f} foi sacado com sucesso!")

        else:
            print("Operação Falhou! O Valor informado é inválido. ")

    elif opcao == "3":
        print("\n********************EXTRATO********************")
        print(f"\nNão foram realizadas movimentações. "if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("\n***********************************************")

    elif opcao == "0":
        print("Saindo...")
        break
    
    else:
        print("Oparação inválida, por favor selecione novamente a operação desejada.")
