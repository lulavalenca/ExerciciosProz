"""
38) Faça um programa que calcule o terno pitagórico a, b, c, para o qual
a + b + c = 1000. Um termo pitagórico é um conjunto de três números
naturais, a, b, c, para a qual,
    a² + b² = c²
Por exemplo,
    3² + 4² = 9 + 16 = 25 = 5²

1 Exemplo    

def encontrar_terno_pitagorico():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c
            
a, b, c = encontrar_terno_pitagorico()

print("O terno pitagorico tal que a + b + c = 1000 é:", a, b, c)
print("O produto abc é:", a * b * c)


2 EXEMPLO

qtd = 700

for i in range(1, qtd + 1):
    a = 0
    b = 0
    c = 0
    for j in range(1, qtd + 1):
        a = j
        b = i
        c = (a ** 2 + b ** 2) ** 0.5

        if b > a:
            if (a + b + c) == 1000:

                print(f"valor de 'a' = {a}")
                print(f"valor de 'b' = {b}")
                print(f"valor de 'c' = {int(c)}")
                print()


                
3 exemplo

def encontrar_ternos_pitagoricos(soma_alvo):
    ternos = []
    for a in range(1, soma_alvo):
        for b in range(a, soma_alvo):
            c = soma_alvo - a - b
            if a**2 + b**2 == c**2:
                ternos.append((a, b, c))
    return ternos

# Soma alvo
soma_alvo = 1000

# Encontrar os ternos pitagóricos
ternos = encontrar_ternos_pitagoricos(soma_alvo)

# Exibir os resultados
print(f"Ternos pitagóricos onde a + b + c = {soma_alvo}:")
for terno in ternos:
    print(terno)

# Calcular e exibir o produto dos ternos
produtos = [a * b * c for a, b, c in ternos]
print(f"\nProdutos dos ternos pitagóricos:")
for produto in produtos:
    print(produto)


"""

def encontrar_ternos_pitagoricos(soma_alvo):
    ternos = []
    for a in range(1, soma_alvo):
        for b in range(a, soma_alvo):
            c = soma_alvo - a - b
            if a**2 + b**2 == c**2:
                ternos.append((a, b, c))
    return ternos

# Solicitar ao usuário que insira a soma alvo
soma_alvo = int(input("Digite a soma alvo para encontrar os ternos pitagóricos: "))

# Encontrar os ternos pitagóricos
ternos = encontrar_ternos_pitagoricos(soma_alvo)

# Exibir os resultados
print(f"Ternos pitagóricos onde a + b + c = {soma_alvo}:")
for terno in ternos:
    print(terno)

# Calcular e exibir o produto dos ternos
produtos = [a * b * c for a, b, c in ternos]
print(f"\nProdutos dos ternos pitagóricos:")
for produto in produtos:
    print(produto)




""""""