"""
21 Faça um programa que receba dois números. Calcule e mostre:
⚫ a soma dos números pares desse intervalo de números, incluindo os números digi- tados;
⚫ a multiplicação dos números impares desse intervalo, incluindo os digitados;

#############/ EXEMPLO 1 \###################
# Função para verificar se um número é par
def eh_par(numero):
    return numero % 2 == 0

# Função para calcular a soma dos números pares
def soma_numeros_pares(inicio, fim):
    soma = 0
    for i in range(inicio, fim + 1):
        if eh_par(i):
            soma += i
    return soma

# Função para calcular a multiplicação dos números ímpares
def multiplicacao_numeros_impares(inicio, fim):
    multiplicacao = 1
    for i in range(inicio, fim + 1):
        if not eh_par(i):
            multiplicacao *= i
    return multiplicacao

# Função principal
def main():
    # Entrada dos números
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))

    # Cálculo e exibição da soma dos números pares
    soma_pares = soma_numeros_pares(inicio, fim)
    print("A soma dos números pares no intervalo é:", soma_pares)

    # Cálculo e exibição da multiplicação dos números ímpares
    multiplicacao_impares = multiplicacao_numeros_impares(inicio, fim)
    print("A multiplicação dos números ímpares no intervalo é:", multiplicacao_impares)

# Chamada da função principal
if __name__ == "__main__":
    main()

#############/ EXEMPLO 2 \###################

# Função para verificar se um número é par
def eh_par(numero):
    return numero % 2 == 0

# Função principal
def main():
    # Entrada dos números
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))

    # Inicialização das variáveis para armazenar a soma dos números pares e a multiplicação dos números ímpares
    soma_pares = 0
    multiplicacao_impares = 1

    # Cálculo da soma dos números pares e da multiplicação dos números ímpares
    for i in range(inicio, fim + 1):
        if eh_par(i):
            soma_pares += i
        else:
            multiplicacao_impares *= i

    # Exibição dos resultados
    print("A soma dos números pares no intervalo é:", soma_pares)
    print("A multiplicação dos números ímpares no intervalo é:", multiplicacao_impares)

# Chamada da função principal
if __name__ == "__main__":
    main()


#############/ EXEMPLO 3 \###################

# Função para verificar se um número é par
def eh_par(numero):
    return numero % 2 == 0

# Função principal
def main():
    # Entrada dos números
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))

    # Inicialização das variáveis para armazenar a soma dos números pares e a multiplicação dos números ímpares
    soma_pares = 0
    multiplicacao_impares = 1

    # Inicialização do contador
    contador = inicio

    # Cálculo da soma dos números pares e da multiplicação dos números ímpares
    while contador <= fim:
        if eh_par(contador):
            soma_pares += contador
        else:
            multiplicacao_impares *= contador
        contador += 1

    # Exibição dos resultados
    print("A soma dos números pares no intervalo é:", soma_pares)
    print("A multiplicação dos números ímpares no intervalo é:", multiplicacao_impares)

# Chamada da função principal
if __name__ == "__main__":
    main()



    

"""


def eh_par(par):
    return par % 2 == 0

def main():
    
    inicio = int(input("Digite o numero inicial do intervalo: "))
    fim = int(input("Digite o numero final do intervalo: " ))


    soma_pares = 0
    multiplicacao_impares = 1 

    for i in range(inicio, fim + 1):
        if eh_par(i):
            soma_pares += i
        else:
            multiplicacao_impares *= i 

    print("A soma dos numeros pares no intervalo:", soma_pares)
    print("A multiplicacao dos numeros impares no intervalo é:", multiplicacao_impares) 

if __name__ == "__main__":
    main()              



# Função para verificar se um número é par
def eh_par(numero):
    return numero % 2 == 0

# Função principal
def main():
    # Entrada dos números
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))

    # Inicialização das variáveis para armazenar a soma dos números pares e a multiplicação dos números ímpares
    soma_pares = 0
    multiplicacao_impares = 1

    # Inicialização do contador
    contador = inicio

    # Cálculo da soma dos números pares e da multiplicação dos números ímpares
    while contador <= fim:
        if eh_par(contador):
            soma_pares += contador
        else:
            multiplicacao_impares *= contador
        contador += 1

    # Exibição dos resultados
    print("A soma dos números pares no intervalo é:", soma_pares)
    print("A multiplicação dos números ímpares no intervalo é:", multiplicacao_impares)

# Chamada da função principal
if __name__ == "__main__":
    main()
