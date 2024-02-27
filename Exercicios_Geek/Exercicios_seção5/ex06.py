numero1 = int(input("Digite o primeiro numero inteiro: "))
numero2 = int(input("Digite o segundo numero inteiro: "))

if numero1 > numero2:
    maior = numero1
    diferenca = numero1 - numero2
else:
    maior = numero2
    diferenca = numero2 - numero1

print(f"O maior número é: {maior}")
print(f"A diferença entre os numero é: {diferenca}")    