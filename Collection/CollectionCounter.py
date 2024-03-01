"""
Modulo Collections - Counter

Collections -> High-Performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections 
Counter que é parecido com um dicionario, contendo como chave o 
elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.


# Realizando o import 

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 2: 4, 3: 3, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou um chave e colocou como valor a quantidade de ocorêcias.

# Exemplo 2 

print(Counter('Luiz Valença)'))
# Counter({'a': 2, 'L': 1, 'u': 1, 'i': 1, 'z': 1, ' ': 1, 'V': 1, 'l': 1, 'e': 1, 'n': 1, 'ç': 1, ')': 1})

# Exemplo 3

#texto = Poucos lugares no mundo passaram por uma miscigenação tão intensa quanto o Brasil.
Os portugueses já trouxeram para o Brasil séculos de integração genética e cultural de povos europeus, como os povos celta, romano, germânico e lusitano. 
Embora os portugueses sejam basicamente uma população europeia, sete séculos de convivência com mouros do norte da África e com judeus deixaram um importante legado a este povo. 
No Brasil, uma parte substancial dos colonizadores portugueses se miscigenou com índios e negros africanos, em um processo muito importante para a formação do País. 
A esse e a outros processos somou-se o processo de imigração de muitos mais europeus. Da metade do século XIX à metade do século XX, a nação recebeu cerca de cinco milhões de imigrantes europeus, em sua maioria portugueses, italianos, espanhóis e alemães. 
Um dos resultados da soma desses processos é a atual composição da população brasileira. Em 2008, 48% da população brasileira se considera branca, 44% se identifica como parda e 7% se considera negra.

palavras = texto.split()

#print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5)) #

"""

from collections import Counter

