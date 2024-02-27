"""
Questão 24

Leia um valor de área em metros quadrados e m² e apresente-o
convertido em acres. A fórmula de conversão é: A = M * 0,000247, sendo M
a área em metros quadrados e A área em acres.

"""

areaMetros = float(input("Digite a área em metros quadrados: "))

areaAcres = areaMetros * 0.000247

print("A area do terreno em acres é: ",areaAcres, "AQ")