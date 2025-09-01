# sistema_bancario_otimizado.py

# Funções do sistema bancário
def criar_usuario(usuarios, cpf, nome, data_nascimento, endereco):
    if any(u["cpf"] == cpf for u in usuarios):
        print("Usuário já cadastrado!")
        return False
    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")
    return True

def criar_conta(contas, agencia, numero_conta, usuarios, cpf):
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado, criação de conta falhou!")
        return False
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "saques_realizados": 0
    })
    print("Conta criada com sucesso!")
    return True

def depositar(conta, valor):
    if valor <= 0:
        print("Valor inválido para depósito.")
        return False
    conta["saldo"] += valor
    conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
    print("Depósito realizado com sucesso!")
    return True

def sacar(conta, valor, limite_saque, limite_diario):
    if valor <= 0:
        print("Valor inválido para saque.")
        return False
    if valor > conta["saldo"]:
        print("Saldo insuficiente!")
        return False
    if valor > limite_saque:
        print("Saque excede o limite permitido!")
        return False
    if conta["saques_realizados"] >= limite_diario:
        print("Número máximo de saques atingido!")
        return False

    conta["saldo"] -= valor
    conta["extrato"].append(f"Saque: R$ {valor:.2f}")
    conta["saques_realizados"] += 1
    print("Saque realizado com sucesso!")
    return True

def mostrar_extrato(conta):
    print("\n========== EXTRATO ==========")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for item in conta["extrato"]:
            print(item)
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("=============================")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
    for c in contas:
        print(f"Agência: {c['agencia']}, Conta: {c['numero_conta']}, Titular: {c['usuario']['nome']}")

def encontrar_conta(contas, numero_conta):
    return next((c for c in contas if c["numero_conta"] == numero_conta), None)

# Função principal do sistema
def main():
    usuarios = []
    contas = []
    agencia_padrao = "0001"
    numero_conta = 1
    limite_saque = 500
    limite_diario = 3

    while True:
        opcao = input("""
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[l] Listar Contas
[q] Sair
=> """).strip()

        if opcao == "d":
            num_conta = int(input("Informe o número da conta: "))
            conta = encontrar_conta(contas, num_conta)
            if conta:
                valor = float(input("Valor do depósito: "))
                depositar(conta, valor)
            else:
                print("Conta não encontrada!")

        elif opcao == "s":
            num_conta = int(input("Informe o número da conta: "))
            conta = encontrar_conta(contas, num_conta)
            if conta:
                valor = float(input("Valor do saque: "))
                sacar(conta, valor, limite_saque, limite_diario)
            else:
                print("Conta não encontrada!")

        elif opcao == "e":
            num_conta = int(input("Informe o número da conta: "))
            conta = encontrar_conta(contas, num_conta)
            if conta:
                mostrar_extrato(conta)
            else:
                print("Conta não encontrada!")

        elif opcao == "nu":
            cpf = input("Informe o CPF: ").strip()
            nome = input("Informe o nome completo: ").strip()
            data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
            endereco = input("Informe o endereço: ").strip()
            criar_usuario(usuarios, cpf, nome, data_nasc, endereco)

        elif opcao == "nc":
            cpf = input("Informe o CPF do titular: ").strip()
            if criar_conta(contas, agencia_padrao, numero_conta, usuarios, cpf):
                numero_conta += 1

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar o banco. Até logo!")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
