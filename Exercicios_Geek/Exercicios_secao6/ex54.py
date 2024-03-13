"""
54) Faça um programa que receba um número inteiro maior do que 1,
e verifique se o número fornecido é primo ou não.



def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número inteiro maior do que 1: "))
if eh_primo(n):
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")


"""