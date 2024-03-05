"""
41) Faça um programa que calcula a associação em paralelo de dois resistores
R1 e R2 fornecidos pelo usuário via teclado. O programa fica pedindo estes
valores e calculando até que o usuário entre com um valor para resistência igual a zero.




"""

while True:

    r1 = float(input("Digite o valor do resistor R1 (ou 0 para encerrar): "))

    if r1 == 0:
        print("Programa encerrado.")
        break

    r2 = float(input("Digite o valor do resistor R2: "))

    if r2 <= 0:
        print("Valor inválido para o resistor R2. Tente novamente.")
        continue

    resistencia_paralelo = (r1 * r2) / (r1 + r2)

    print("A resistencia equivalente em paralelo é:", resistencia_paralelo)