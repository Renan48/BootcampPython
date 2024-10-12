menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
limiteSaques = 3

while True:
    opcao = input(menu).lower() 

    if opcao == "d": 
        while True:
            valor = float(input("Insira o valor do Depósito:  "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor de depósito inválido. Tente novamente.")
            
            continuar = input("Deseja continuar depositando? (s/n): ").lower()
            if continuar != "s":
                break 

    elif opcao == "s":  
        if saldo <= 0:
            print("Sem Saldo Para Saque.")
        else:
            while True:
                
                if numeroSaques >= 3:
                    print("Número máximo de saques excedido.")
                    break
            
                valor = float(input("Informe o valor do Saque: "))

                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite

                if excedeu_saldo:
                    print("Saldo insuficiente.")
                elif excedeu_limite:
                    print("O valor do saque excede o limite.")
                elif valor > 0:
                    saldo -= valor
                    numeroSaques += 1
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("O valor informado é inválido. Tente novamente.")
                
                continuar = input("Deseja continuar sacando? (s/n): ").lower()
                if continuar != "s":
                    break  
                
    elif opcao == "e":  
        print("\n         EXTRATO         ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("              ")

    elif opcao == "q": 
        print("Obrigado por usar nosso sistema bancário!")
        break

    else:
        print("Operação inválida.")
