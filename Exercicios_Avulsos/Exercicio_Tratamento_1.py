def calcular_imc (peso, altura):

    if (peso < 0) or (altura < 0):
        raise Exception("Valores preenchidos incorretamente")
    
    imc = (peso) / (altura * altura)

    return imc