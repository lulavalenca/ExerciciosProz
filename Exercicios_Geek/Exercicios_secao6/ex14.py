"""
14. Faça um programa que leia um número inteiro positivo par N e 
imprima todos os números pares de 0 até N em ordem decrescente.


"""

N = int(input("Digite um numero inteiro positivo par: "))

print("Numeros pares de", N, "até 0 em ordem decrescente: ")

for i in range(N, -1, -2):
    print(i)