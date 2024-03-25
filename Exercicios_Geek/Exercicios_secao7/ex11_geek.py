"""
11) Faça um programa que preencha um vetor com 10 números reais, 
calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

1 Exemplo do codigo 
numeros = [float(input(f"Digite o numero real {i+1}: ")) for i in range(10)]

contagem_negativos = sum(1 for numero in numeros if numero < 0 )

soma_positivos = sum(numero for numero in numeros if numero > 0 )

print(f"Quantidade de numeros negativos: {contagem_negativos}")
print(f"Soma dos numeros positivos: {soma_positivos}")

"""
numero_negativos = 0
soma_positivos = 0

vetor = []
for i in range(10):
    numero = float(input("Digite um numero: "))
    vetor.append(numero)

for numero in vetor:
    if numero < 0:
        numero_negativos += 1
    else:
        soma_positivos += numero

print("Quantidade de numeros negativos:", numero_negativos)
print("Soma dos numeros positivos:", soma_positivos)                

