"""
Um produto vai sofrer aumento de acordo com a tabela abaixo.
Leia o preço antigo e calcule e escreva o preço novo, e escreva uma mensagem
em função do preço novo (de acordo com a segunda tabela).

    |     PREÇO ANTIGO     |   PERCENTUAL DE AUMENTO  |
    | até R$50             |            5%            |
    | entre R$50 e R$ 100  |           10%            |
    | acima de R$100       |           15%            |


    |          PREÇO NOVO              |   MENSAGEM   |
    | até R$80                         | Barato       |
    | entre R%80 e R$120 (inclusive)   | Normal       |
    | entre R$ 120 e R$200 (inclusive) | Caro         |
    | acima de R$200                   | Muito caro   |


# Lê o preço antigo do produto
preco_antigo = float(input("Digite o preço antigo do produto: R$ "))

# Calcula o percentual de aumento de acordo com a tabela
if preco_antigo <= 50:
    percentual_aumento = 0.05  # 5%
elif preco_antigo <= 100:
    percentual_aumento = 0.10  # 10%
else:
    percentual_aumento = 0.15  # 15%

# Calcula o preço novo
preco_novo = preco_antigo * (1 + percentual_aumento)

# Determina a mensagem conforme o preço novo
if preco_novo <= 80:
    mensagem = "Barato"
elif preco_novo <= 120:
    mensagem = "Normal"
elif preco_novo <= 200:
    mensagem = "Caro"
else:
    mensagem = "Muito caro"

# Exibe o preço novo e a mensagem
print(f"Preço novo: R$ {preco_novo:.2f}")
print("Mensagem:", mensagem)



"""

preco_antigo = float(input("Digite o preço antigo do produto: R$ "))

if preco_antigo <= 50:
    precentual_aumento = 0.05
elif preco_antigo <= 100:
    percentual_aumento = 0.10
else:
    percentual_aumento = 0.15

preco_novo = preco_antigo * (1 + percentual_aumento)

if preco_novo <= 80:
    mensagem = "Barato"
elif preco_novo <= 120:
    mensagem = "Normal"
elif preco_novo <= 200:
    mensagem = "Caro"
else:
    mensagem = "Muito caro"        

print(f"Preço novo: R${preco_novo:.2f}")
print("Mensagem:", mensagem)