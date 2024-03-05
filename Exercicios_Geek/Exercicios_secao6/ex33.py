"""
﻿

33. Dados e dois números inteiros positivos, i ej, 
diferentes de 0, 
imprimir em ordem crescente os primeiros naturais que são múltiplos de i ou de je ou de ambos. 
Exemplo: Para n = 6,i=2e j = 3 a saída deverá ser: 0,2,3,4,6,8.



"""

def multiplos_ordenados(n, i, j):
    multiplos = []
    numero = 0
    while len(multiplos) < n:
        if numero % i == 0 or numero % numero % j == 0:
            multiplos.append(numero)
        numero += 1
    return multiplos

# 
n = int(input("Digite o valor de n: "))
i = int(input("digite o valor de i: "))
j = int(input("digite o valor de j: "))

resultado = multiplos_ordenados(n, i, j)
print("Os primeiros", n, "multiplos de", i, "ou", j, "ou ambos, em ordem crescente, são:", resultado)
