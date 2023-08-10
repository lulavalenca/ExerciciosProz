def calculadora(num1, num2, operacao):
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
      if num2 != 0:
            resultado = num1 / num2
      else:
          raise ValueError("Divisão por zero não é permitida.")
    else:
        raise ValueError("Operação inválida. Escolha entre '+', '-', '*' ou '/' .")

    return resultado

# Exemplos de uso:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a opreção (+, -, *, /): ")

try:
    resultado = calculadora(num1, num2, operacao)
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")    