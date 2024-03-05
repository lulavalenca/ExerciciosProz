"""
50. Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centimetros por ano. 
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.

"""

# Alturas iniciais e taxas de crescimento de Chico e Zé
altura_chico = 1.50
crescimento_chico = 0.02
altura_ze = 1.10
crescimento_ze = 0.03

# Contador de anos
anos = 0

# Enquanto Zé for menor que Chico
while altura_ze <= altura_chico:
    # Ambos crescem
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    # Contabiliza mais um ano
    anos += 1

print(f"Serão necessários {anos} anos para que Zé seja maior que Chico.")
