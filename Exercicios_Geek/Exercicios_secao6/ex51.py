"""
51) Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais.
Em 1996 recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem
ao dobro do ano anterior. Faça programa que determine o salário atual do funcionário.


"""

salario = 2000
aumento = 0.015

ano_inicial = 1995
ano_atual = 2024

while ano_atual > ano_inicial:
    if ano_inicial > 1995:
        aumento *= 2
    salario += salario * aumento
    ano_inicial += 1

print(f"O salario atual do funcionario é de R$ {salario:.2f}")    
