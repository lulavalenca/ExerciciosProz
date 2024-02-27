"""""" # Exemplo 1 de codigo 

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF do usuário: ")
    endereco = input("Informe o endereço (logradouro, cidade/estado): ")
    
    # Verificar se o CPF já existe na lista de usuários
    cpfs = [usuario['cpf'] for usuario in usuarios]
    if cpf in cpfs:
        print("CPF já cadastrado.")
        return usuarios
    
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    
    print("Usuário cadastrado com sucesso.")
    return usuarios

def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    
    # Verificar se o CPF existe na lista de usuários
    cpfs = [usuario['cpf'] for usuario in usuarios]
    if cpf not in cpfs:
        print("CPF não encontrado.")
        return contas
    
    # Encontrar o usuário com o CPF informado
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    
    # Criar nova conta
    numero_conta = len(contas) + 1
    contas.append({
        'agencia': "0001",
        'numero_conta': numero_conta,
        'usuario': usuario
    })
    
    print(f"Conta corrente criada com sucesso para {usuario['nome']}. Número da conta: {numero_conta}")
    return contas

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo=saldo, valor=valor, extrato=extrato)
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, 
                                               numero_saques=numero_saques, limite_saques=limite_saques)
    
    elif opcao == "e":
        extrato(saldo=saldo, extrato=extrato)
    
    elif opcao == "u":
        usuarios = criar_usuario(usuarios)
    
    elif opcao == "c":
        contas = criar_conta(contas, usuarios)
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
"""


""" #  Exemplo 2 





