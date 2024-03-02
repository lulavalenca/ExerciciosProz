"""
13 - Faça um programa que leia um número inteiro positivo par N e 
imprima todos os números pares de 0 até N em ordem crescente. 

"""



N = int(input("Digite um numero inteiro positivo par: "))

print("Numeros paras de 0 até", N, "em ordem crescente: ")

for i in range(0, N + 1, 2):
    print(i)

    