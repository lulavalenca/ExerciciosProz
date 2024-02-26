"""
26) Leia um valor de área em metros quadrados m² e apresente-o convertido
em hectares. A fórmula de conversão é: H = M * 0.0001, sendo M a área em
metros quadrados e H a área em hectares

01areaMetros = float(input("Digite a área em metros quadrados por favor: "))

areaHectare = areaMetros * 0.0001

print("Area em hectare: ",areaHectare)

metros_quadrados = float(input("Digite o valor da área em metros quadrados m³: "))

hectares = metros_quadrados * 0.0001

print("\n================================")
print("A área em hectares é"+ hectares)


"""

metros_quadrados = float(input("Digite o valor da área em metros quadrados m³: "))

hectares = metros_quadrados * 0.0001

print("\n================================")
print("A área em hectares é " + str(hectares))