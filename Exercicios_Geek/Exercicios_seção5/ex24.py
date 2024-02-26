# Define o dicionário com as taxas de imposto de cada estado
taxas_imposto = {
    "MG": 0.07,
    "SP": 0.12,
    "RJ": 0.15,
    "MS": 0.08
}

# Lê o valor do produto e o estado destino fornecidos pelo usuário
valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite o estado destino (MG, SP, RJ ou MS): ").upper()

# Verifica se o estado destino é válido e calcula o preço final do produto
if estado_destino in taxas_imposto:
    taxa_imposto_estado = taxas_imposto[estado_destino]
    preco_final = valor_produto * (1 + taxa_imposto_estado)
    print(f"O preço final do produto para o estado {estado_destino} é R$ {preco_final:.2f}.")
else:
    print("Estado inválido. Por favor, digite um estado válido.")
