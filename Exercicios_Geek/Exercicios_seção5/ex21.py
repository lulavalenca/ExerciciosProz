"""
print("Escolha a opção:")
print("1 - Soma de 2 números.")
print("2 - Diferença entre 2 números (maior pelo menor).")
print("3 - Produto entre 2 números.")
print("4 - Divisão entre 2 números (o denominador não pode ser zero).")

opcao = int(input("Opção: "))

if opcao == 1:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é {resultado}.")
elif opcao == 2:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: ")) 
    diferenca = abs(num1 - num2)
    print(f"A diferença entre {num1} e {num2} é {diferenca}.")
elif opcao == 3:
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    resultados = num1 * num2
    print(f"O produto de  {num1} e {num2} é {resultados}.")
elif opcao == 4:
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: ")) 
    if num2 != 0:
        resultados = num1 / num2
        print(f"A divisão {num1} por {num2} é {resultado}.")
    else:
        print("O denominador não pode ser zero.")    
else:
    # Mensagem de erro para opção inválida
    print("Opção inválida.")
"""

print("Escolha a opção:")
print("1 - Soma de 2 números.")
print("2 - Diferença entre 2 números (maior pelo menor).")
print("3 - Produto entre 2 números.")
print("4 - Divisão entre 2 números (o denominador não pode ser zero).")

opcao = int(input("Opção: "))

if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é {resultado}.")
elif opcao == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: ")) 
    diferenca = abs(num1 - num2)
    print(f"A diferença entre {num1} e {num2} é {diferenca}.")
elif opcao == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"O produto de {num1} e {num2} é {resultado}.")
elif opcao == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: ")) 
    if num2 != 0:
        resultado = num1 / num2
        print(f"A divisão de {num1} por {num2} é {resultado}.")
    else:
        print("O denominador não pode ser zero.")
else:
    # Mensagem de erro para opção inválida
    print("Opção inválida.")
