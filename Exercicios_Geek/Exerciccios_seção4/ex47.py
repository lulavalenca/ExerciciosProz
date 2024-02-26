"""
1- Exemplo 
numeroInteiro = int(input("digite um numero de 4 digito entre(1000 a 9999): "))
if 1000 <= numeroInteiro  <= 9999:
    numero_str = str(numeroInteiro)

    for digito in numero_str:
        print(digito)
else:
    print("Número inválido. Por favor, digite um número de quatro dígitos entre 1000 e 9999.")       

2- Exemplo

# Leitura do número inteiro de quatro dígitos
numero = int(input("Digite um número inteiro de quatro dígitos (entre 1000 e 9999): "))

# Verificando se o número está dentro do intervalo válido
if 1000 <= numero <= 9999:
    # Extraindo e imprimindo cada dígito do número
    milhar = numero // 1000
    centena = (numero // 100) % 10
    dezena = (numero // 10) % 10
    unidade = numero % 10
    
    print(milhar)
    print(centena)
    print(dezena)
    print(unidade)
else:
    print("Número inválido. Por favor, digite um número de quatro dígitos entre 1000 e 9999.")



"""

# Leitura do número inteiro de quatro dígitos
numero = int(input("Digite um número inteiro de quatro dígitos (entre 1000 e 9999): "))

# Verificando se o número está dentro do intervalo válido
if 1000 <= numero <= 9999:
    # Extraindo e imprimindo cada dígito do número
    milhar = numero // 1000
    centena = (numero // 100) % 10
    dezena = (numero // 10) % 10
    unidade = numero % 10
    
    print(milhar)
    print(centena)
    print(dezena)
    print(unidade)
else:
    print("Número inválido. Por favor, digite um número de quatro dígitos entre 1000 e 9999.")
