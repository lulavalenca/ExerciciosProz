"""
47. Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
adição (opção 1)
⚫ subtração (opção 2)
⚫ multiplicação (opção 3)
⚫ divisão (opção 4).
⚫ saída (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, 
a exibição do resultado e a volta ao menu de opções. 
O programa só termina quando for escolhida a opção de saída (opção 5).

1 Exemplo 




"""

# Função para realizar a adição
def adicao(a, b):
    return a + b

# Função para realizar a subtração
def subtracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Função principal
def main():
    while True:
        print("\nMENU DE OPÇÕES:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado da adição: {adicao(num1, num2)}")
        elif opcao == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado da subtração: {subtracao(num1, num2)}")
        elif opcao == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado da multiplicação: {multiplicacao(num1, num2)}")
        elif opcao == '4':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número (diferente de zero): "))
            print(f"Resultado da divisão: {divisao(num1, num2)}")
        elif opcao == '5':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chamada da função principal
main()

