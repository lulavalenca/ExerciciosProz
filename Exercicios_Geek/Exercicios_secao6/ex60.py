"""
60) Faça um programa que leia vários números, calcule e mostre:

(a) A soma dos números digitados
(b) A quantidade de números digitados
(c) A média dos números digitados
(d) O maior número digitado
(e) O menor número digitado
(f) A média dos números pares

Finalize a entrada de dados caso o usuário informe o valor 0.




"""

numeros = []
pares = []

while True:
    numero = int(input("Digite um numero (0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)

print(f"(a) A soma dos numeros digitados é {sum(numeros)}")
print(f"(b) A quantidade de numeros digitados é {len(numeros)}")
print(f"(c) A mêdia dos numeros digitados é {sum(numeros) / len(numeros)}")
print(f"(d) O maior numero digitado é {max(numeros)}")
print(f"(e) O menor número digitado é {min(numeros)}")
print(f"(f) A média dos numeros pares é {sum(pares) / len(pares) if pares else 0}")