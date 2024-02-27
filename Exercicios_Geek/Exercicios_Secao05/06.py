"""
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

maior_numero = max(numero1, numero2)

diferenca = abs(numero1 - numero2)

print("O maior numero é: ", maior_numero)7

print("A diferença entre os numeros é: ", diferenca)
"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
if num1 > num2:
    print(f"O primeiro numero é maior que o segundo e a diferença entre ele é de {num1 - num2}.")
elif num1 == num2:
    print("Os dois numeros são iguais!")
else:
    print(f"O segundo numero é maior que o primeiro numero e a diferença entre ele é de {num1 - num2}.")        