"""
27. Leia 10 números inteiros e armazene em um vetor. 
Em seguida escreva os elementos que são primos e suas respectivas posições no vetor.



"""

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros = [int(input(f"Digite o numeo {i+1}:")) for i in range(10)]

primos = [(num, i)for i, num in enumerate(numeros) if eh_primo(num)]

for num, pos in primos:
    print(f"O numero {num} na posição {pos} é primo.")