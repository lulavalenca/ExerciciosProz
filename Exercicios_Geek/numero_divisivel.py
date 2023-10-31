# Recebe um número inteiro como entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 3 ou 5, mas não simultaneamente
if (numero % 3 == 0 or numero % 5 == 0) and not (numero % 3 == 0 and numero % 5 == 0):
    print(f"O número {numero} é divisível por 3 ou 5, mas não por ambos simultaneamente.")
else:
    print(f"O número {numero} não atende aos critérios especificados.")
