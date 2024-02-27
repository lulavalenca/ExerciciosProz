# Função para calcular o número de garrafas no segundo dia
def calcular_garrafas_segundo_dia(N, K):
    # Calcula o número de garrafas cheias que o cliente ganha no primeiro dia
    garrafas_cheias_primeiro_dia = N // K
    # Calcula o número total de garrafas vazias no primeiro dia
    total_garrafas_primeiro_dia = N + garrafas_cheias_primeiro_dia
    # Calcula o número total de garrafas no segundo dia
    total_garrafas_segundo_dia = total_garrafas_primeiro_dia - garrafas_cheias_primeiro_dia * K
    return total_garrafas_segundo_dia

# Função principal
def main():
    # Lê o número de casos de teste
    T = int(input())
    
    # Para cada caso de teste
    for _ in range(T):
        # Lê os valores de N e K
        N, K = map(int, input().split())
        # Calcula e imprime o número de garrafas no segundo dia
        print(calcular_garrafas_segundo_dia(N, K))

# Chama a função principal
if __name__ == "__main__":
    main()
