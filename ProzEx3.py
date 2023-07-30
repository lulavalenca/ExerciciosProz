def calculadora(num1, num2, operacao):
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
            return "Erro: Divisão por zero não é permitida."
    else:
        return 0

# Solicita ao usuário os números e a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação desejada (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

# Chama a função e exibe o resultado
resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)
