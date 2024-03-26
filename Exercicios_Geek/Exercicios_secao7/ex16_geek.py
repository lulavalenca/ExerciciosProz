"""
16) Faça um programa que leia um vetor de 5 posições para números reais e,
depois, um código inteiro, Se o código for zero, finalize o programa;
se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem
inversa. Caso, o código for diferente de 1 e 2 escreva uma mensagem informando
que o código é inválido

# 1 Exemplo de codigo

def mostrar_ordem_direta(vetor):
    print("vetor na ordem direta:", vetor)

def mostrar_ordem_inversa(vetor):
    print("Vetor na ordem inversa:", vetor[::-1]) 

vetor = []
for i in range(5):
    valor = float(input("Digite o valor da posição {}:".format(i + 1)))
    vetor.append(valor)

codigo = int(input("Digite o codigo (0 para sair, 1 para ordem direta, 2 para ordem inversa): ")) 

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    mostrar_ordem_direta(vetor)
elif codigo == 2:
    mostrar_ordem_inversa(vetor)
else:
    print("Codigo inválido. Por favor, digite 0, 1 ou 2.")            


# 2 Exemplo de codigo 

# Declaração de variáveis
vetor = []
codigo = None

# Leitura dos valores do vetor
for i in range(5):
    numero = float(input("Digite um número: "))
    vetor.append(numero)

# Leitura do código
while codigo not in [0, 1, 2]:
    try:
        codigo = int(input("Digite o código (0 para sair, 1 para ordem direta, 2 para ordem inversa): "))
    except ValueError:
        print("Código inválido. Digite um número inteiro.")

# Exibição do vetor
if codigo == 1:
    print("Vetor na ordem direta:", vetor)
elif codigo == 2:
    print("Vetor na ordem inversa:", vetor[::-1])
else:
    print("Programa finalizado.")



"""

def mostrar_ordem_direta(vetor):
    print("vetor na ordem direta:", vetor)

def mostrar_ordem_inversa(vetor):
    print("Vetor na ordem inversa:", vetor[::-1]) 

vetor = []
for i in range(5):
    valor = float(input("Digite o valor da posição {}:".format(i + 1)))
    vetor.append(valor)

codigo = int(input("Digite o codigo (0 para sair, 1 para ordem direta, 2 para ordem inversa): ")) 

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    mostrar_ordem_direta(vetor)
elif codigo == 2:
    mostrar_ordem_inversa(vetor)
else:
    print("Codigo inválido. Por favor, digite 0, 1 ou 2.")            

# 2 Exemplo de codigo     
    
# Declaração de variáveis
vetor = []
codigo = None

# Leitura dos valores do vetor
for i in range(5):
    numero = float(input("Digite um número: "))
    vetor.append(numero)

# Leitura do código
while codigo not in [0, 1, 2]:
    try:
        codigo = int(input("Digite o código (0 para sair, 1 para ordem direta, 2 para ordem inversa): "))
    except ValueError:
        print("Código inválido. Digite um número inteiro.")

# Exibição do vetor
if codigo == 1:
    print("Vetor na ordem direta:", vetor)
elif codigo == 2:
    print("Vetor na ordem inversa:", vetor[::-1])
else:
    print("Programa finalizado.")
