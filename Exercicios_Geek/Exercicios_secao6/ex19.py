"""
19 - Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compõem o número 

"""



numero = int(input("Digite um número inteiro entre 100 e 999: "))

if 100 <= numero <= 999:
    numero_str = str(numero)
    print("Algarismos do número:")
    for algarismo in numero_str:
        print(algarismo)
else:
    print("Número fora do intervalo permitido.")
