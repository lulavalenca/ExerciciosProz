"""
24. Faça um programa que leia dez conjuntos de dois valores, 
o primeiro representando o número do aluno e o segundo representando a sua altura em metros. 
Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo e do mais alto, 
juntamente com suas alturas.

# 1 Exemplo de codigo 

numero_aluno_mais_baixo = numero_aluno_mais_alto = None
altura_mais_baixa = altura_mais_alta = None

for i in range(10):
    numero_aluno = int(input(f"Digite o numero do aluno {i+1}: "))
    altura = float(input(f"Digite a altura do aluno {i+1} em metros: "))

    if altura_mais_baixa is None or altura < altura_mais_baixa:
        altura_mais_baixa = altura
        numero_aluno_mais_baixo = numero_aluno
    if altura_mais_alta is None or altura > altura_mais_alta:
        altura_mais_alta = altura
        numero_aluno_mais_alto = numero_aluno    

print("O aluno mais baixo é o numero", numero_aluno_mais_baixo,"com altura de", altura_mais_baixa, "metros.")        
print("O aluno mais alto é o numero", numero_aluno_mais_alto,"com altura de", altura_mais_alta, "metros.")        

"""

numero_aluno_mais_baixo = numero_aluno_mais_alto = None
altura_mais_baixa = altura_mais_alta = None

for i in range(10):
    numero_aluno = int(input(f"Digite o numero do aluno {i+1}: "))
    altura = float(input(f"Digite a altura do aluno {i+1} em metros: "))

    if altura_mais_baixa is None or altura < altura_mais_baixa:
        altura_mais_baixa = altura
        numero_aluno_mais_baixo = numero_aluno
    if altura_mais_alta is None or altura > altura_mais_alta:
        altura_mais_alta = altura
        numero_aluno_mais_alto = numero_aluno    

print("O aluno mais baixo é o numero", numero_aluno_mais_baixo,"com altura de", altura_mais_baixa, "metros.")        
print("O aluno mais alto é o numero", numero_aluno_mais_alto,"com altura de", altura_mais_alta, "metros.")        

# 2 EXEMPLO DE CODIGO

# Função para ler os dados dos alunos
def ler_dados_alunos():
    alunos = []
    for i in range(10):
        numero_aluno = int(input("Digite o número do aluno {}: ".format(i + 1)))
        altura_aluno = float(input("Digite a altura do aluno {} (em metros): ".format(i + 1)))
        alunos.append((numero_aluno, altura_aluno))
    return alunos

# Função para encontrar o aluno mais baixo e o mais alto
def encontrar_alunos_extremos(alunos):
    mais_baixo = min(alunos, key=lambda x: x[1])
    mais_alto = max(alunos, key=lambda x: x[1])
    return mais_baixo, mais_alto

# Função para imprimir os resultados
def imprimir_resultados(mais_baixo, mais_alto):
    print("\nAluno mais baixo:")
    print("Número do aluno:", mais_baixo[0])
    print("Altura:", mais_baixo[1], "metros")
    print("\nAluno mais alto:")
    print("Número do aluno:", mais_alto[0])
    print("Altura:", mais_alto[1], "metros")

# Ler os dados dos alunos
alunos = ler_dados_alunos()

# Encontrar o aluno mais baixo e o mais alto
mais_baixo, mais_alto = encontrar_alunos_extremos(alunos)

# Imprimir os resultados
imprimir_resultados(mais_baixo, mais_alto)
