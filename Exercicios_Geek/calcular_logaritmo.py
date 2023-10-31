import math

# Recebe um número inteiro como entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é negativo
if numero < 0:
    print("Número inválido.")
else:
    # Calcula o logaritmo natural (ln) do número positivo
    resultado = math.log(numero)
    print(f"O logaritmo natural do número é {resultado:.2f}")
