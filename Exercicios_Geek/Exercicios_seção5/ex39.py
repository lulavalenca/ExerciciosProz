"""

Uma empresa decide dar um aumento aos seus funcionários de acordo com uma
tabela que consideraa o salário atual e o tempo de serviço de cada funcionário.
Os funcionários com menor salário terão um aumento proporcionalmente maior do que
os funciopnários com um salário maior, e conforme o tempo de serviço na empresa, cada
funcionário irá receber um bônus adicional de salário. Faça um programa que leia:

    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionário na empresa (número de anos de trabalho na
    empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima
o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha
direito a nenhum aumento.

    |   Salário Atual   |   Reajuste    | Tempo de Serviço |  Bônus     |
    | Até 500,00        |     25%       | Abaixo de 1 ano  | Sem bônus  |
    | Até 1000,00       |     20%       | De 1 a 3 anos    |  100,00    |
    | Até 1500,00       |     15%       | De 4 a 6 anos    |  200,00    |
    | Até 2000,00       |     10%       | De 7 a 10 anos   |  300,00    |
    | Acima de 2000,00  | Sem reajuste  | Mais de 10 anos  |  500,00    |




# Função para calcular o reajuste do salário
def calcular_reajuste(salario_atual):
    if salario_atual <= 500:
        return 0.25
    elif salario_atual <= 1000:
        return 0.20
    elif salario_atual <= 1500:
        return 0.15
    elif salario_atual <= 2000:
        return 0.10
    else:
        return 0

# Função para calcular o bônus baseado no tempo de serviço
def calcular_bonus(tempo_servico):
    if tempo_servico < 1:
        return 0
    elif 1 <= tempo_servico <= 3:
        return 100
    elif 4 <= tempo_servico <= 6:
        return 200
    elif 7 <= tempo_servico <= 10:
        return 300
    else:
        return 500

# Leitura do salário atual e do tempo de serviço
salario_atual = float(input("Digite o salário atual do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário (em anos): "))

# Cálculo do reajuste e do bônus
reajuste = calcular_reajuste(salario_atual)
bonus = calcular_bonus(tempo_servico)

# Verificação se o funcionário tem direito a algum aumento
if reajuste == 0 and bonus == 0:
    print("O funcionário não tem direito a nenhum aumento.")
else:
    # Cálculo do salário reajustado
    novo_salario = salario_atual * (1 + reajuste) + bonus

    # Exibição do resultado
    print(f"O salário reajustado do funcionário é: R$ {novo_salario:.2f}")




"""

# Leitura do salário atual e do tempo de serviço
salario_atual = float(input("Digite o salário atual do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário (em anos): "))

# Definição das taxas de reajuste e bônus de acordo com a tabela
if salario_atual <= 500:
    reajuste = 0.25
    bonus = 0 if tempo_servico < 1 else None
elif salario_atual <= 1000:
    reajuste = 0.20
    bonus = 100 if 1 <= tempo_servico <= 3 else None
elif salario_atual <= 1500:
    reajuste = 0.15
    bonus = 200 if 4 <= tempo_servico <= 6 else None
elif salario_atual <= 2000:
    reajuste = 0.10
    bonus = 300 if 7 <= tempo_servico <= 10 else None
else:
    reajuste = 0
    bonus = 500 if tempo_servico > 10 else None

# Verificação se o funcionário tem direito a algum aumento
if reajuste == 0 and bonus is None:
    print("O funcionário não tem direito a nenhum aumento.")
else:
    # Cálculo do salário reajustado
    novo_salario = salario_atual * (1 + reajuste)
    if bonus is not None:
        novo_salario += bonus

    # Exibição do resultado
    print(f"O salário reajustado do funcionário é: R$ {novo_salario:.2f}")
