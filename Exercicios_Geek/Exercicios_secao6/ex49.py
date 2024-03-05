"""
﻿

49. O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário. 
Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, 
pois está rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, 
que está rendendo 5% ao mês. 
Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. 
Teste com outros valores para as taxas.

1 EXemplo 

def calcular_meses(salario_carlos, taxa_carlos, taxa_joao):
    salario_joao = salario_carlos / 3
    meses = 0

    while salario_joao < salario_carlos:
        salario_carlos += salario_carlos * taxa_carlos
        salario_joao += salario_joao * taxa_joao
        meses += 1

    return meses

salario_carlos = float(input("Digite o salário de Carlos: "))
taxa_carlos = float(input("Digite a taxa de rendimento de Carlos (em decimal): "))
taxa_joao = float(input("Digite a taxa de rendimento de João (em decimal): "))

meses = calcular_meses(salario_carlos, taxa_carlos, taxa_joao)
print(f"São necessários {meses} meses para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.")


"""

def calcular_meses(salario_carlos, taxa_carlos, taxa_joao):
    salario_joao = salario_carlos / 3
    saldo_carlos = salario_carlos
    saldo_joao = salario_joao
    meses = 0

    while saldo_joao < saldo_carlos:
        saldo_carlos += saldo_carlos * taxa_carlos
        saldo_joao += saldo_joao * taxa_joao
        meses += 1

    return meses

salario_carlos = float(input("Digite o salário de Carlos: "))
taxa_carlos = float(input("Digite a taxa de rendimento de Carlos (em decimal): "))
taxa_joao = float(input("Digite a taxa de rendimento de João (em decimal): "))

meses = calcular_meses(salario_carlos, taxa_carlos, taxa_joao)
print(f"São necessários {meses} meses para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.")
