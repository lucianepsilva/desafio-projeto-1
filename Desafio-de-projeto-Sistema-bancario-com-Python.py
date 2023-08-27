menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """


saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = "" 

while True:

    opcao = input (menu)

    if(opcao == "1"):
        valor = float(input("Informe o valor do depósito: "))

        if(valor > 0):
            saldo = saldo + valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido")

    elif(opcao == "2"):
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        if(excedeu_saldo):
            print("Você não possui saldo suficiente para essa operação.")

        elif(excedeu_limite):
            print("O valor solicitado excede o limite permitido por operação.")

        elif(excedeu_limite_saques):
            print("O número de saques diário foi excedido.")

        elif(valor > 0):
            saldo = saldo - valor
            numero_saques = numero_saques + 1 
            extrato = extrato + f"Saque: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido: ")

    elif(opcao == "3"):
        print("\n-------------------EXTRATO-------------------")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------------------------")

    elif(opcao == "0"):
        break

    else:
        print("Erro! Por favor selecionar uma opção válida. ")




