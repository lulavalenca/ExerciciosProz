"""
# Função para mostrar o menu de opções
def mostrar_menu():
    print("Escolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

# Função para realizar a operação escolhida pelo usuário
def calcular(operacao, num1, num2):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"

# Mostra o menu
mostrar_menu()

# Solicita a escolha da operação
opcao = int(input("Digite o número da operação desejada: "))

# Solicita os valores para operação
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Calcula o resultado da operação
resultado = calcular(opcao, valor1, valor2)

# Exibe o resultado
print("Resultado:", resultado)


"""

operacao = input("Escolha a Operação ['*']['/']['+']['-']: ")

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

print()
if operacao == '*':
    print(f"O resultado da operação escolhida: {num1 * num2}")
elif operacao == '/':
    print(f"O resultado da operação escolhida: {num1 / num2}")
elif operacao == '+':
    print(f"O resultado da operação escolhida: {num1 + num2}")
elif operacao == '-':
    print(f"O resultado da operação escolhida: {num1 - num2}")
else:
    print("Operação inválida")             
