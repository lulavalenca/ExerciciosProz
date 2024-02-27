"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da
comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados
sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e
escreva o custo ao consumidor

    |      CUSTO DE FÁBRICA          | % DO DISTRIBUIDOR | % DOS IMPOSTOS |
    | até R$12.000,00                |         5         |    isento      |
    | entre R$12.000,00 e 25.000,00  |        10         |      15        |
    | acima de R$25.000,00           |        15         |      20        |



"""

def calcular_custo_consumidor(custo_fabrica):
    if custo_fabrica <= 12000:
        comissao = custo_fabrica * 0.05
        impostos = 0
    elif 12000 < custo_fabrica <= 25000:
        comissao = custo_fabrica * 0.10
        impostos = custo_fabrica * 0.15
    else:
        comissao = custo_fabrica * 0.15
        impostos = custo_fabrica * 0.20
    
    return custo_fabrica + comissao + impostos

custo_fabrica = float(input("Digite o custo de fábrica do carro: R$"))
custo_consumidor = calcular_custo_consumidor(custo_fabrica)
print(f"O custo ao consumidor do carro é: R${custo_consumidor:.2f}")
