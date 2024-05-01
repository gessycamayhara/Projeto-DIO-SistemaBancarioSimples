menu = """
 
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [4] Sair
 
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        
        valor = float(input("Digite o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"\nDeposito: R$ {valor:.2f}"
            print("Deposito realizado com sucesso! Aguarde o seu comprovante.")
            
        else:
            print("Valor inválido! Por favor, digite um valor positivo.")
            
    elif opcao == "2":
        
        valor = float(input("Digite o valor do saque: "))
        
        if valor > 0 and valor <= limite:
            if valor <= saldo:
                numero_saques = numero_saques + 1
                
                if numero_saques > LIMITES_SAQUES:
                    print("Limite de saque diário alcançado. Tente novamente amanhã!")
                    
                else:
                    saldo -= valor
                    print("Saque efetuado com sucesso!")            
                    extrato += f"\nSaque: R$ {valor:.2f}"

            else:
                print("Saldo insuficiente!")    
        else:
            print("O valor não está dentro do limite. Por favor, digite um novo valor.")    
        
    elif opcao == "3":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:    
            print("\n=============== Extrato ===============")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=========================================")
    
    elif opcao == "4":
        break    
    
    else:
        print("Opção inválida, por favor digite novamente a opção desejada!")  
                      