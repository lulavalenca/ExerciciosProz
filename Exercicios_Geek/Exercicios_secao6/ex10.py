"""
10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.



"""

soma = 0
contador = 0 
numero = 0

while contador < 10:
    if numero % 2 == 0:
        soma += numero
        contador += 1
    numero += 1
print("A soma dos 50 primeiros números pares é: ", soma)

