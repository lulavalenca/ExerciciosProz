# Exibe o menu de opções
print("Escolha a opção:")
print("1 - Soma de 2 números.")
print("2 - Diferença entre 2 números (maior pelo menor).")
print("3 - Produto entre 2 números.")
print("4 - Divisão entre 2 números (o denominador não pode ser zero).")

# Recebe a opção do usuário
opcao = input("Opção: ")

# Verifica a opção escolhida
if opcao == "1":
    # Opção 1: Soma de 2 números
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 + numero2
    print(f"A soma dos números é: {resultado}")
elif opcao == "2":
    # Opção 2: Diferença entre 2 números
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = abs(numero1 - numero2)
    print(f"A diferença entre os números é: {resultado}")
elif opcao == "3":
    # Opção 3: Produto entre 2 números
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 * numero2
    print(f"O produto dos números é: {resultado}")
elif opcao == "4":
    # Opção 4: Divisão entre 2 números (com verificação de divisão por zero)
    numero1 = float(input("Digite o numerador: "))
    numero2 = float(input("Digite o denominador: "))
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"A divisão dos números é: {resultado}")
    else:
        print("Erro: Divisão por zero.")
else:
    print("Opção inválida. Escolha uma opção de 1 a 4.")
