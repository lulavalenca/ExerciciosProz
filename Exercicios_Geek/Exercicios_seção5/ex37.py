"""
As tarifas de certo parque de estacionamento são as seguintes:

    - 1ª e 2ª hora - R$1,00 cada
    - 3ª e 4ª hora - R$1,40 cada
    - 5ª hora e seguintes - R$2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por execesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste
sao apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12,50 representará 'dez para a uma da parte'. Pretende-se
criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva
na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida
se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada
for supeiror à da partida, isso não é uma situação de erro, antes siginificará que
a partida ocorreu no dia seguinte ao chegada.


def calcular_preco(chegada, partida):
    hora_chegada, min_chegada = chegada
    hora_partida, min_partida = partida
    
    minutos_chegada = hora_chegada * 60 + min_chegada
    minutos_partida = hora_partida * 60 + min_partida
    
    duracao_minutos = minutos_partida - minutos_chegada
    duracao_horas = duracao_minutos // 60
    
    if duracao_minutos % 60 > 0:
        duracao_horas += 1
    
    if duracao_horas <= 2:
        preco = duracao_horas * 1.00
    elif duracao_horas <= 4:
        preco = 2 * 1.00 + (duracao_horas - 2) * 1.40
    else:
        preco = 2 * 1.00 + 2 * 1.40 + (duracao_horas - 4) * 2.00
    
    return preco

# Leitura dos momentos de chegada e partida
chegada = tuple(map(int, input("Informe o momento de chegada (hh mm): ").split()))
partida = tuple(map(int, input("Informe o momento de partida (hh mm): ").split()))

# Cálculo do preço cobrado pelo estacionamento
preco = calcular_preco(chegada, partida)

# Exibição do preço
print(f"O preço cobrado pelo estacionamento é R${preco:.2f}")



"""


def calcular_preco(chegada, partida):
    hora_chegada, min_chegada = chegada
    hora_partida, min_partida = partida
    
    minutos_chegada = hora_chegada * 60 + min_chegada
    minutos_partida = hora_partida * 60 + min_partida
    
    duracao_minutos = minutos_partida - minutos_chegada
    duracao_horas = duracao_minutos // 60
    
    if duracao_minutos % 60 > 0:
        duracao_horas += 1
    
    if duracao_horas <= 2:
        preco = duracao_horas * 1.00
    elif duracao_horas <= 4:
        preco = 2 * 1.00 + (duracao_horas - 2) * 1.40
    else:
        preco = 2 * 1.00 + 2 * 1.40 + (duracao_horas - 4) * 2.00
    
    return preco

# Leitura dos momentos de chegada e partida
chegada = tuple(map(int, input("Informe o momento de chegada (hh mm): ").split()))
partida = tuple(map(int, input("Informe o momento de partida (hh mm): ").split()))

# Cálculo do preço cobrado pelo estacionamento
preco = calcular_preco(chegada, partida)

# Exibição do preço
print(f"O preço cobrado pelo estacionamento é R${preco:.2f}")
