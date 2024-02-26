# Lê a distância em km
distancia_km = float(input("Digite a distância percorrida em km: "))

# Lê a quantidade de litros de gasolina consumidos
litros_gasolina = float(input("Digite a quantidade de litros de gasolina consumidos: "))

# Calcula o consumo em km/l
consumo_km_litro = distancia_km / litros_gasolina

# Determina a mensagem com base no consumo
if consumo_km_litro < 8:
    mensagem = "Venda o carro!"
elif 8 <= consumo_km_litro <= 12:
    mensagem = "Econômico!"
else:
    mensagem = "Super econômico!"

# Exibe a mensagem correspondente ao consumo
print(f"Consumo: {consumo_km_litro:.2f} km/l - {mensagem}")
