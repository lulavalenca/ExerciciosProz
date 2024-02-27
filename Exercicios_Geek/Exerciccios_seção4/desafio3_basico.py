def encaixa(A, B):
    # Verifica se o tamanho de B é maior que o tamanho de A
    if len(B) > len(A):
        return "nao encaixa"
    
    # Obtém os últimos dígitos de A com base no tamanho de B
    ultimos_digitos = A[-len(B):]
    
    # Compara os últimos dígitos de A com B
    if ultimos_digitos == B:
        return "encaixa"
    else:
        return "nao encaixa"

def main():
    # Lê o número de casos de teste
    N = int(input())
    
    # Para cada caso de teste
    for _ in range(N):
        # Lê os valores A e B
        A, B = input().split()
        
        # Chama a função encaixa() e imprime o resultado
        print(encaixa(A, B))

if __name__ == "__main__":
    main()
