# Dicionário de taxas de imposto por estado
taxas_imposto = {
    "MG": 0.07,
    "SP": 0.12,
    "RJ": 0.15,
    "MS": 0.08
}

# Recebe o valor do produto como entrada do usuário
valor_produto = float(input("Digite o valor do produto: "))

# Recebe o estado de destino como entrada do usuário
estado_destino = input("Digite o estado de destino (MG, SP, RJ, MS): ").upper()

# Verifica se o estado de destino é válido
if estado_destino in taxas_imposto:
    taxa_imposto = taxas_imposto[estado_destino]
    preco_final = valor_produto * (1 + taxa_imposto)
    print(f"O preço final do produto no estado de {estado_destino} é R${preco_final:.2f}")
else:
    print("Estado de destino inválido. Por favor, escolha um estado válido.")
