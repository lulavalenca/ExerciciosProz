"""
26 - Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.

Exemplo 1

def primeiro_multiplo(numero):
    while True:
        numero += 1
        if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
            return numero

numero_inicial = int(input("Digite um numero inicial: "))

primeiro = primeiro_multiplo(numero_inicial)

print(f"O primeiro multiplo de 11, 13, ou 17 após {numero_inicial} é:", primeiro)


Exemplo 2


def primeiro_multiplo(numero, multiplos):
    while True:
        numero += 1  # Incrementar o número para verificar o próximo
        if any(numero % m == 0 for m in multiplos):
            return numero

try:
    # Solicitar ao usuário que insira o número inicial
    numero_inicial = int(input("Digite um número inicial: "))

    # Solicitar ao usuário que insira os múltiplos desejados, separados por vírgula
    multiplos = list(map(int, input("Digite os múltiplos desejados separados por vírgula: ").split(',')))

    # Encontrar o primeiro múltiplo de acordo com os múltiplos especificados
    primeiro = primeiro_multiplo(numero_inicial, multiplos)

    # Exibir o primeiro múltiplo encontrado
    print(f"O primeiro múltiplo de {', '.join(map(str, multiplos))} após {numero_inicial} é:", primeiro)
except ValueError:
    print("Entrada inválida. Certifique-se de inserir números inteiros.")

    

  
Nesta versão revisada, o usuário pode especificar quais múltiplos deseja procurar após o número inicial, e o código irá encontrar o primeiro múltiplo que corresponde a qualquer um dos múltiplos fornecidos. Além disso, o código agora trata entradas inválidas para garantir uma experiência de usuário mais robusta.

def primeiro_multiplo(numero):
    while True:
        numero += 1
        if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
            return numero

numero_inicial = int(input("Digite um numero inicial: "))

primeiro = primeiro_multiplo(numero_inicial)

print(f"O primeiro multiplo de 11, 13, ou 17 após {numero_inicial} é:", primeiro)


"""




def primeiro_multiplo(numero, multiplos):
    while True:
        numero += 1
        if any(numero % m == 0 for m in multiplos):
            return numero

try:
    numero_inicial = int(input("Digite um numero inicial: "))

    multiplos = list(map(int, input("Digite os multiplos desejados separados por virgula: ").split(',')))

    primeiro = primeiro_multiplo(numero_inicial, multiplos)

    print(f"O primeiro multiplo de {', '.join(map(str, multiplos))} após {numero_inicial} é:", primeiro)
except ValueError:
    print("Entrada invalida. Certifique-se de inserir numeros inteiros.")        