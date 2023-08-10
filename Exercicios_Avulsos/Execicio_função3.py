def fibonacci_recursivo(n):
    if n <= 0:
        raise ValueError("O valor de 'n deve ser maior que zero.")
    elif n == 1:
        return 0 
    elif n == 2:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
# Exemplo de uso:
n = int(input("Digite o valor de N para calcular o termo Fibonacci: "))
resultado = fibonacci_recursivo(n)
print(f"O {n}-ésimo termo da sequência de Fibonacci é: {resultado}")    