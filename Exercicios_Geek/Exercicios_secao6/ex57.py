"""

57) Faça um programa que conte quantos números primos existem entre a
e b, onde a e b são números informados pelo usuário.



1 Exemplo 

def calcular_numero_primos(a, b):
  numero_primos = 0
  for numero in range(a, b + 1):
    if eh_primo(numero):
      numero_primos += 1
  return numero_primos

def eh_primo(numero):
  if numero <= 1:
    return False
  for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
      return False
  return True

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

numero_primos = calcular_numero_primos(a, b)

print(f"Existem {numero_primos} números primos entre {a} e {b}")



"""

def calcular_numero_primos(a, b):
  numero_primos = 0
  for numero in range(a, b + 1):
    if eh_primo(numero):
      numero_primos += 1
  return numero_primos

def eh_primo(numero):
  if numero <= 1:
    return False
  for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
      return False
  return True

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

numero_primos = calcular_numero_primos(a, b)

print(f"Existem {numero_primos} números primos entre {a} e {b}")
