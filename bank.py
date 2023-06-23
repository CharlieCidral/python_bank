# User accounts data structure (example)
user_accounts = {
    "user1": {
        "senha": "password1",
        "saldo": 1000.0,
        "extrato": "",
        "historico_saldo": [],
        "nome": "João da Silva",
        "numero_conta": "123456789",
        "contato": "joao.silva@email.com",
        "type": "admin"  # Type of account
    },
    "user2": {
        "senha": "password2",
        "saldo": 500.0,
        "extrato": "",
        "historico_saldo": [],
        "nome": "Maria Oliveira",
        "numero_conta": "987654321",
        "contato": "maria.oliveira@email.com",
        "type": "regular"  # Type of account
    },
    # Add more user accounts as needed
}

menu = """
[t] Transferir
[b] Informações da conta
[d] Depositar
[s] Sacar
[e] Extrato
[h] Histórico de saldo
[u] Atualizar informações pessoais
[q] Sair

=> """

saldo = user_accounts["user1"]["saldo"]
extrato = user_accounts["user1"]["extrato"]
historico_saldo = user_accounts["user1"]["historico_saldo"]
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

nome = user_accounts["user1"]["nome"]
numero_conta = user_accounts["user1"]["numero_conta"]
contato = user_accounts["user1"]["contato"]
account_type = user_accounts["user1"]["type"]

def authenticate():
    password = input("Digite sua senha: ")
    return password

authenticated = False
while not authenticated:
    password_attempt = authenticate()
    if password_attempt == user_accounts["user1"]["senha"]:
        authenticated = True
    else:
        print("Senha incorreta. Tente novamente.")

while True:
    opcao = input(menu)

    if opcao == "t":
        # Transfer funds implementation
        valor = float(input("Informe o valor da transferência: "))
        conta_destino = input("Informe o número da conta de destino: ")

        # Check if the recipient account exists
        if conta_destino in user_accounts:
            # Check if the transfer amount is valid
            if valor > 0:
                # Check if the sender's account has sufficient balance
                if valor <= saldo:
                    # Perform the transfer
                    saldo -= valor
                    extrato += f"Transferência para a conta {conta_destino}: R$ {valor:.2f}\n"
                    # Update the sender's account statement
                    user_accounts["user1"]["extrato"] = extrato
                    # Update the recipient's account balance
                    user_accounts[conta_destino]["saldo"] += valor

                    # Update balance history
                    historico_saldo.append(saldo)
                    user_accounts["user1"]["historico_saldo"] = historico_saldo

                    print("Transferência realizada com sucesso.")
                else:
                    print("Transferência falhou! Saldo insuficiente.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Conta de destino não encontrada.")
        pass
    elif opcao == "b":
        # Account information implementation
        print("\n========= Informações da Conta =========")
        print("Nome do titular: ", nome)
        print("Número da conta: ", numero_conta)
        print("Contato: ", contato)
        print("Tipo de conta: ", account_type)
        print("Saldo: R$ {:.2f}".format(saldo))
        print("========================================")
        pass
    elif opcao == "d":
        # Deposit implementation
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            # Update balance history
            historico_saldo.append(saldo)
            user_accounts["user1"]["historico_saldo"] = historico_saldo

        else:
            print("Operação falhou! O valor informado é inválido.")
        pass
    elif opcao == "s":
        # Withdraw implementation
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            # Update balance history
            historico_saldo.append(saldo)
            user_accounts["user1"]["historico_saldo"] = historico_saldo

        else:
            print("Operação falhou! O valor informado é inválido.")
        pass
    elif opcao == "e":
        # Account statement implementation
        print("\n================ Extrato ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
        pass
    elif opcao == "h":
        # Balance history implementation
        print("\n=========== Histórico de Saldo ===========")
        for i, saldo_historico in enumerate(historico_saldo):
            print(f"Transação {i+1}: R$ {saldo_historico:.2f}")
        print("=========================================")
        pass
    elif opcao == "u":
        if account_type == "admin":
            admin_password = authenticate()
            if admin_password == user_accounts["user1"]["senha"]:
                print("\n========= Atualizar informações pessoais =========")
                new_nome = input("Digite o novo nome: ")
                if input("Deseja alterar o número da conta? (S/N): ").lower() == "s":
                    new_numero_conta = input("Digite o novo número da conta: ")
                    user_accounts["user1"]["numero_conta"] = new_numero_conta
                    numero_conta = new_numero_conta  # Update local variable
                new_contato = input("Digite o novo contato: ")
                user_accounts["user1"]["nome"] = new_nome
                user_accounts["user1"]["contato"] = new_contato
                nome = new_nome  # Update local variable
                contato = new_contato  # Update local variable
                print("Informações pessoais atualizadas com sucesso.")
                print("=================================================")
            else:
                print("Senha incorreta. Apenas o administrador pode atualizar as informações pessoais.")
        else:
            print("Apenas o administrador pode atualizar as informações pessoais.")
    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
