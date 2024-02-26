"""
1- Exemplo

# Recebendo o número de três dígitos do usuário
numero = int(input("Digite um número de três dígitos (entre 100 e 999): "))

# Verificando se o número está dentro do intervalo válido
if 100 <= numero <= 999:
    # Extraindo os dígitos do número
    centenas = numero // 100
    dezenas = (numero // 10) % 10
    unidades = numero % 10

    # Invertendo os dígitos
    numero_invertido = unidades * 100 + dezenas * 10 + centenas

    # Exibindo o número invertido
    print(f"O número invertido é: {numero_invertido}")
else:
    print("Por favor, digite um número válido de três dígitos.")

# 2 - Exemplo

# Leitura do número inteiro de três dígitos
numero = int(input("Digite um número inteiro de três dígitos (entre 100 e 999): "))

# Verificando se o número está dentro do intervalo válido
if 100 <= numero <= 999:
    # Convertendo o número em uma string para facilitar a manipulação dos dígitos
    numero_str = str(numero)
    
    # Invertendo os dígitos do número lido
    numero_invertido = int(numero_str[::-1])
    
    # Imprimindo o número gerado
    print(f"Número Gerado: {numero_invertido}")
else:
    print("Número inválido. Por favor, digite um número de três dígitos entre 100 e 999.")



"""



# Leitura do número inteiro de três dígitos
numero = int(input("Digite um número inteiro de três dígitos (entre 100 e 999): "))

# Verificando se o número está dentro do intervalo válido
if 100 <= numero <= 999:
    # Convertendo o número em uma string para facilitar a manipulação dos dígitos
    numero_str = str(numero)
    
    # Invertendo os dígitos do número lido
    numero_invertido = int(numero_str[::-1])
    
    # Imprimindo o número gerado
    print(f"Número Gerado: {numero_invertido}")
else:
    print("Número inválido. Por favor, digite um número de três dígitos entre 100 e 999.")
