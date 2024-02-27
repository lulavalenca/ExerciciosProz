"""
1 - Exemplo de execução 

importancia_total = 780000.00

quantia_primeiro_ganhador = importancia_total * 0.46
quantia_segundo_ganhador = importancia_total * 0.32
quantia_terceiro_ganhador = importancia_total - quantia_primeiro_ganhador - quantia_segundo_ganhador

print("Quantia ganha pelo primeiro ganhador:", quantia_primeiro_ganhador)
print("Quantia ganha pelo segundo ganhador:", quantia_segundo_ganhador)
print("Quantia ganha pelo terceiro ganhador:", quantia_terceiro_ganhador)




"""

quantia_total = 780000.00

porcentagem_primeiro = 0.46
porcentagem_segundo = 0.32

quantia_primeiro = quantia_total * porcentagem_primeiro
quantia_segundo = quantia_total * porcentagem_segundo
quantia_terceiro = quantia_total - quantia_primeiro - quantia_segundo

print(f"Quantia do primeiro ganhador: R$ {quantia_primeiro:.2f}")
print(f"Quantia do segundo ganhador: R$ {quantia_segundo:.2f}")
print(f"Quantia do terceiro ganhador: R$ {quantia_terceiro:.2f}")