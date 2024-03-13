"""
56) Faça um programa que calcule a soma de todos os números primos
abaixo de dois milhões.


1 Exemplo

def calcular_soma_primos(limite):
  soma = 0
  for numero in range(2, limite + 1):
    if eh_primo(numero):
      soma += numero
  return soma

def eh_primo(numero):
  if numero <= 1:
    return False
  for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
      return False
  return True

limite = 2000000

soma_primos = calcular_soma_primos(limite)

print(f"A soma dos números primos abaixo de {limite} é {soma_primos}")


2 exemplo

def calcular_soma_primos(limite):
    soma = 0
    for numero in range(2, limite + 1):
        if eh_primo(numero):
            soma += numero
        return soma

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        return True

limite = 350000000

soma_primo = calcular_soma_primos(limite)

print(f"A soma dos numeros primos abaixo de {limite} é {soma_primo}")

"""

qtd = 2000000

soma =  0 

for i in range(1, qtd):
    cont = 0 

    for j in range(1, i +1):
        if (i % 1 == 0 ) and (i % j == 0):
            cont += 1

    if cont <= 2:
        soma += i  

print(f"A soma de todos os numeros primos abaixo de dois milhôes: {soma}")             