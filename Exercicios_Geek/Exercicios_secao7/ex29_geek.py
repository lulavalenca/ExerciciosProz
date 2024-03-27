"""
29. Faça um programa que receba 6 números inteiros e mostre:
• Os números pares digitados;
• A soma dos números pares digitados;
• Os números impares digitados;
• A quantidade de números ímpares digitados;

########################################################################


"""

# 1 Exemplo de codigo

numeros = [int(input(f"Digite o numero {i+1}:")) for i in range(6)]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

soma_pares = sum(pares)

quantidade_impares = len(impares)

print("Numeros oares digitados: ", pares)
print("Soma dos numeros pares digitados:", soma_pares)
print("Numeros impares digitados:", impares)
print("Quantidade de numeros impares digitados:", quantidade_impares)


# 2 Exemplo de codigo

numeros= []
for i in range(6):
    numero = int(input("Digite o {}º numero inteiro: ".format(i+1)))
    numeros.append(numero)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)


soma_pares = sum(pares)

print("Numeros pares digitados:",pares)
print("Soma dos numeros pares:", soma_pares)
print("Numeros impares digitados:", impares)
print("Quantidade de numeros impares:", len(impares))
