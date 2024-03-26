"""
18) 18) Faça um programa que leia um vetor de 10 números. Leia um
número x. Conte os múltiplos de um número inteiro x num vetor
e mostre-os na tela.


# 1 Exemplo de codigo 

vetor = []
x = None
multiplos = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    vetor.append(numero)

while not x:
    try:
       x = int(input("Digite um numero x: "))
    except ValueError:
        print("Valor invalido. Digite um numero inteiro.")

for numero in vetor:
    if numero % x == 0:
        multiplos.append(numero)

if multiplos:
    print("Multiplos de {} no vetor: {}".format(x, multiplos))
else:
    print("Não existem multiplos de {} no vetor.".format(x))                      


# 2 Exemplo codigo 
    
   # Função para contar e mostrar os múltiplos de x em um vetor
def contar_multiplos(vetor, x):
    multiplos = [numero for numero in vetor if numero % x == 0]
    quantidade = len(multiplos)
    return multiplos, quantidade

# Lê os valores do vetor
vetor = []
for i in range(10):
    valor = int(input("Digite o {}º número do vetor: ".format(i + 1)))
    vetor.append(valor)

# Lê o número inteiro x
x = int(input("Digite o número inteiro x para encontrar seus múltiplos: "))

# Conta e mostra os múltiplos de x no vetor
multiplos, quantidade = contar_multiplos(vetor, x)
if quantidade > 0:
    print("Múltiplos de", x, "encontrados no vetor:", multiplos)
    print("Quantidade de múltiplos de", x, "no vetor:", quantidade)
else:
    print("Não foram encontrados múltiplos de", x, "no vetor.")
 


"""

# 1 Exemplo de codigo 

vetor = []
x = None
multiplos = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    vetor.append(numero)

while not x:
    try:
       x = int(input("Digite um numero x: "))
    except ValueError:
        print("Valor invalido. Digite um numero inteiro.")

for numero in vetor:
    if numero % x == 0:
        multiplos.append(numero)

if multiplos:
    print("Multiplos de {} no vetor: {}".format(x, multiplos))
else:
    print("Não existem multiplos de {} no vetor.".format(x))                      


# 2 Exemplo codigo 
    
   # Função para contar e mostrar os múltiplos de x em um vetor
def contar_multiplos(vetor, x):
    multiplos = [numero for numero in vetor if numero % x == 0]
    quantidade = len(multiplos)
    return multiplos, quantidade

# Lê os valores do vetor
vetor = []
for i in range(10):
    valor = int(input("Digite o {}º número do vetor: ".format(i + 1)))
    vetor.append(valor)

# Lê o número inteiro x
x = int(input("Digite o número inteiro x para encontrar seus múltiplos: "))

# Conta e mostra os múltiplos de x no vetor
multiplos, quantidade = contar_multiplos(vetor, x)
if quantidade > 0:
    print("Múltiplos de", x, "encontrados no vetor:", multiplos)
    print("Quantidade de múltiplos de", x, "no vetor:", quantidade)
else:
    print("Não foram encontrados múltiplos de", x, "no vetor.")
 