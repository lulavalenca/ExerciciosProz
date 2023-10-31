# Recebe dois números como entrada do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os números e exibe o maior ou a mensagem "Números iguais"
if numero1 > numero2:
    print(f"O maior número é {numero1}.")
elif numero2 > numero1:
    print(f"O maior número é {numero2}.")
else:
    print("Números iguais.")
