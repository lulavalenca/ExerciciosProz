def identificar_animal(palavra1, palavra2, palavra3):
    if palavra1 == "vertebrado":
        if palavra2 == "ave":
            if palavra3 == "carnivoro":
                return "aguia"
            elif palavra3 == "onivoro":
                return "pomba"
        elif palavra2 == "mamifero":
            if palavra3 == "onivoro":
                return "homem"
            elif palavra3 == "herbivoro":
                return "vaca"
    elif palavra1 == "invertebrado":
        if palavra2 == "inseto":
            if palavra3 == "hematofago":
                return "pulga"
            elif palavra3 == "herbivoro":
                return "lagarta"
        elif palavra2 == "anelideo":
            if palavra3 == "hematofago":
                return "sanguessuga"
            elif palavra3 == "onivoro":
                return "minhoca"

def main():
    # Lê as três palavras que definem o tipo de animal
    palavra1 = input()
    palavra2 = input()
    palavra3 = input()

    # Chama a função para identificar o animal e imprime o resultado
    print(identificar_animal(palavra1, palavra2, palavra3))

if __name__ == "__main__":
    main()
