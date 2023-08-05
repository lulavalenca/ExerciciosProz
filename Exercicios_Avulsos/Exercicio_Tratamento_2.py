print("Programa Imc")
rodar = True
while(rodar):

    try:
        print("Digite o seu peso")
        
        peso = float(input())

        print("Digite a sua altura")

        alt = float(input())

        imc = imc_function(peso, alt)

        print(imc)

        rodar = False

    except:
        print("Dados incorretos")

print("finalizado")            