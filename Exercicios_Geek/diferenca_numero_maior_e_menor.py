# Recebe dois números inteiros como entrada do usuário
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Determina qual número é o maior
if numero1 > numero2:
    maior = numero1
    diferenca = numero1 - numero2
else:
    maior = numero2
    diferenca = numero2 - numero1

# Exibe o maior número e a diferença
print(f"O maior número é {maior}.")
print(f"A diferença entre os números é {abs(diferenca)}.")
