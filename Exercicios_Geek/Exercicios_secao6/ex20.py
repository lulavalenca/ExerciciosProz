"""
20 - 

"""

total_numeros = 0
total_pares = 0

while True:
    numero = int(input("Digite um numero inteiro (1000 para encerar): "))

    if numero == 1000:
        break

    total_numeros += 1

    if numero % 2 == 0:
        total_pares += 1

print("Total de numeros lidos: ", total_numeros)
print("Total de numeros pares: ", total_pares)        