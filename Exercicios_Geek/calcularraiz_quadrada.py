# Recebe um número como entrada do usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo ou negativo
if numero > 0:
    raiz_quadrada = numero ** 0.5
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
elif numero < 0:
    print("Número inválido. O número fornecido é negativo.")
else:
    print("O número fornecido é zero.")
