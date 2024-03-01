"""
1 - Exercicio:
Faça um programa que determine e mostre os cincos primeiros
múltiplos de 3, considerando números maiores que 0

1 - Exemplo 

cont =  0 
for i in range(1, 1000):
    if cont >= 5:
        break

    if i % 3 == 0:
        print(i)
        cont += 1

2 - Exemplo 


num_multiplos = 0

numero = 1

while num_multiplos < 5:
    if numero % 3 == 0:
        
       print(numero)

       num_multiplos += 1

    numero += 1            

3 - Exemplo


# Inicializa o número de múltiplos encontrados
num_multiplos = 0

# Loop for para encontrar os cinco primeiros múltiplos de 3
for numero in range(1, 100):  # Podemos limitar a busca até 100, por exemplo
    # Verifica se o número é um múltiplo de 3
    if numero % 3 == 0:
        # Imprime o número
        print(numero)
        # Incrementa o número de múltiplos encontrados
        num_multiplos += 1
    # Se encontramos os cinco múltiplos, saímos do loop
    if num_multiplos == 5:
        break


"""


num_multiplos = 0

for numero in range(1, 100):
    if numero % 3 == 0:
        print(numero)

        num_multiplos += 1

    if num_multiplos == 5:
        break    