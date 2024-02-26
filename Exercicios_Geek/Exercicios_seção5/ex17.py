"""
# Solicita a entrada dos valores do trapézio
base_maior = float(input("Digite o valor da base maior do trapézio: "))
base_menor = float(input("Digite o valor da base menor do trapézio: "))
altura = float(input("Digite o valor da altura do trapézio: "))

# Verifica se os valores das bases são maiores que zero
if base_maior > 0 and base_menor > 0:
    # Calcula a área do trapézio
    area_trapezio = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {area_trapezio}")
else:
    print("Erro: Os valores das bases devem ser maiores que zero.")

"""


base_menor = float(input("Digite o tamanho da base menor do trapézio em cm: "))
base_maior = float(input("Digite o tamanho da base maior do trapézio em cm: "))
altura = float(input("Digite a altura do trapézio em cm: "))

print()
if (base_menor > 0) and (base_maior > 0) and (altura > 0):

    area = ((base_maior + base_menor) * altura)/ 2
    print("A área do trapezio é %.1fcm²" % area)

else:
    print("valor(es) inválido(s)")