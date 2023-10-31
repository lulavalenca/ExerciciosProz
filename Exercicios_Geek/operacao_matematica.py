# Função para realizar a operação de adição
def adicao(a, b):
    return a + b

# Função para realizar a operação de subtração
def subtracao(a, b):
    return a - b

# Função para realizar a operação de multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a operação de divisão
def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

# Exibe o menu
print("Escolha uma operação matemática:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicita a escolha da operação ao usuário
opcao = input("Digite o número da operação desejada: ")

# Verifica a escolha da operação
if opcao in ("1", "2", "3", "4"):
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))

    if opcao == "1":
        resultado = adicao(a, b)
    elif opcao == "2":
        resultado = subtracao(a, b)
    elif opcao == "3":
        resultado = multiplicacao(a, b)
    else:
        resultado = divisao(a, b)

    print(f"O resultado da operação é: {resultado}")
else:
    print("Opção inválida. Escolha uma operação de 1 a 4.")
