"""
32. Faça um programa que simula o lançamento de dois dados, 
dl e d2, n vezes, e tem como saída o número de cada dado 
e a relação entre eles (>,<,=) de cada lançamento.





"""
import random

def simular_lancamento_dados(n):
    for _ in range(n):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        print(f"Lançamento: d1 = {d1}, d2 = {d2}", end='')

        if d1 > d2:
            print('d1 > d2')
        elif d1 < d2:
            print('d1 < d2')
        else:
            print('d1 = d2') 

n_lancamentos = int(input("Digite o numero de lançamentos desejado: "))

simular_lancamento_dados(n_lancamentos)