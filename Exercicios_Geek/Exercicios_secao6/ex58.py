"""
58 - . Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário.


"""

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def soma_primos(a, b):
    soma = 0
    for numero in range(a, b+1):
        if eh_primo(numero):
            soma += numero
    return soma

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
soma = soma_primos(a, b)

print(f"A soma dos numeros primos entre {a} e {b} é {soma}.")

# 2 EXEMPLO 

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

soma = 0

for numero in range(a, b+1):
    primo = True

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break    

    if primo:
        soma += numero
        
print(f"A soma dos numeros primos entre {a} e {b} é {soma}. ")