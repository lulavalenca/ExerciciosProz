"""
1- Exemplo 
# Recebe três números como entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Coloca os números em uma lista
numeros = [num1, num2, num3]

# Ordena os números em ordem crescente
numeros_ordem_crescente = sorted(numeros)

# Exibe os números em ordem crescente
print("Números em ordem crescente:")
for numero in numeros_ordem_crescente:
    print(numero)



"""


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

menor = 0 
meio = 0
maior = 0

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        meio = num2
        maior = num3
    else:
        meio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        meio = num1
        maior = num3
    else:
        meio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        meio = num1
        maior = num2
    else:
        meio = num2
        maior = num1 

print("Numero em ordem crescente:")
print(menor)
print(meio)
print(maior)