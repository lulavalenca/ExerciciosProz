"""
Dicionários 

OBS: Em algumas linguagens de programação os dicionário Python são con

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
# Podemos utilizar qualquer tipo de dados (int, float, string, boolean), inclusive lista, tupla, dicionario
# como chaves de dicionario

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionario, pois as mesmas
# São imutaveis.

localidades ={
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7789, 50.5568): 'Escritorio em Nova York',
    (68.4231, 90.0155): 'Escritorio em Recife',
}

print(localidades)
print(type(localidades))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguain'}

# Adiconar elementos em um dicionario


receita = {'jan': 100, 'fev': 250, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 300

print(receita) 

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionario 

# Forma 1 

receita['mai'] = 550

print(receita)

# Forma 2 

receita.update({'mai': 600})

print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2: Em dicionário, Não podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum 

ret = receita.pop('mar')
print(ret)  

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2:

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.

"""

# Imagine que você tem um comercio eletronico, onde temos um carrinho de comprar na qual adicionamos produtos.
"""
Carrinho de compras:
    produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        -nome;
        -quantidade;
        - preço;    

        
# - Poderiamos utilizar uma lista para isso? Sim 

carrinho = []

produto1 = ['Playstation 4', 1, 230.00]
produto2 = ['Playstation 5', 2, 330.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim 

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['Playstation 5', 2, 3300.00]

carrinho = [produto1, produto2]

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 3 - Poderiamos utilizar um Dicionário para isso? sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2330.00}
produto2 = {'nome': 'Playstation 5', 'quantidade': 1, 'preco': 3300.00}

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos pordutos no carrinho e em cada produto
# Podemos ter a certeza sobre cada informação        

Dicionarios em Python: Uma Visão Geral
ChatGPT
Dicionários em Python: Uma Visão Geral

Definição:

Em Python, um dicionário é uma estrutura de dados que armazena pares chave-valor. 
Ele é semelhante a um mapa ou a um conjunto não ordenado de elementos. 
Cada valor armazenado em um dicionário é acessado por meio de uma chave única.

Sintaxe:

python
Copy code
# Criando um dicionário vazio
meu_dicionario = {}

# Criando um dicionário com valores iniciais
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
Acesso a Valores:

python
Copy code
# Acessando valores por chave
nome = pessoa["nome"]  # Resultado: "João"
idade = pessoa["idade"]  # Resultado: 25
Modificando Valores:

python
Copy code
# Modificando valores por chave
pessoa["idade"] = 26
Adicionando Novos Pares Chave-Valor:

python
Copy code
# Adicionando um novo par chave-valor
pessoa["profissao"] = "Engenheiro"
Removendo Pares Chave-Valor:

python
Copy code
# Removendo um par chave-valor
del pessoa["cidade"]
Operações com Dicionários:

python
Copy code
# Verificando se uma chave está no dicionário
tem_chave = "idade" in pessoa  # Resultado: True

# Obtendo todas as chaves e valores
chaves = pessoa.keys()
valores = pessoa.values()

# Iterando sobre chaves e valores
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
Observações Finais:

Os dicionários em Python são mutáveis, o que significa que você pode modificar, 
adicionar e remover itens após a criação.
As chaves em um dicionário devem ser únicas.
Dicionários são frequentemente usados para representar estruturas de dados mais complexas, como configurações, registros ou informações relacionadas.
User
teria mais coisas para adicionar em Dicionario?
ChatGPT
Sim, há algumas outras características e operações que você pode considerar ao trabalhar com dicionários em Python:

Recuperação Segura com get:
Em vez de acessar diretamente um valor por meio de dicionario[chave], você pode usar o método get para recuperar um valor com segurança, evitando erros se a chave não existir.

python
Copy code
idade = pessoa.get("idade", "Chave não encontrada")  # Se "idade" não existir, retorna a mensagem
Definindo Valores Padrão com setdefault:
O método setdefault permite definir um valor padrão para uma chave se ela não existir.

python
Copy code
pessoa.setdefault("profissao", "Desconhecida")  # Define "Desconhecida" se "profissao" não existir
Merging de Dicionários com update:
Você pode mesclar dois dicionários usando o método update.

python
Copy code
dados_adicionais = {"hobbies": ["leitura", "esportes"]}
pessoa.update(dados_adicionais)
Copiando Dicionários:
Para criar uma cópia de um dicionário, você pode usar o método copy ou o construtor dict.

python
Copy code
copia_pessoa = pessoa.copy()
ou

python
Copy code
copia_pessoa = dict(pessoa)
É importante notar que essas cópias são "superficiais". Se o dicionário contiver objetos mutáveis (como listas), as mudanças nesses objetos refletirão em ambas as cópias.

Eliminação Segura com pop:
O método pop remove e retorna um valor associado à chave especificada. Isso é útil para eliminar itens do dicionário com segurança.

python
Copy code
idade = pessoa.pop("idade", None)  # Se "idade" não existir, retorna None
Compreensões de Dicionário:
Assim como as listas, você pode usar compreensões de dicionário para criar dicionários de maneira concisa.

python
Copy code
quadrados = {x: x ** 2 for x in range(5)}
Este exemplo cria um dicionário onde as chaves são números de 0 a 4 e os valores são os quadrados desses números.

Essas são apenas algumas das muitas operações que você pode realizar com dicionários em Python. A flexibilidade e a eficiência dos dicionários fazem deles uma estrutura de dados poderosa em muitos casos de uso.

User
faça um resumo com exemplos oque faz cada coisa e coloque exemplos de como executar cada tópico sobre Mapas em python 
ChatGPT
Certamente! Vamos abordar alguns conceitos sobre "mapas" em Python, utilizando principalmente os dicionários, que são estruturas de dados fundamentais.

Dicionários (Mapas) em Python:
**1. Definindo um Dicionário:

Dicionários em Python são coleções de pares chave-valor.

Exemplo:

python
Copy code
pessoa = {"nome": "João", "idade": 25, "profissao": "Engenheiro"}
2. Acessando Valores:

Os valores são acessados através das chaves.

Exemplo:

python
Copy code
nome = pessoa["nome"]  # Retorna "João"
3. Adicionando e Modificando:

Adicionar ou modificar valores é feito atribuindo um valor a uma chave.

Exemplos:

python
Copy code
pessoa["cidade"] = "São Paulo"  # Adiciona uma nova chave
pessoa["idade"] = 26  # Modifica o valor da chave "idade"
4. Removendo Itens:

O método pop permite remover um item dado sua chave.

Exemplo:

python
Copy code
profissao = pessoa.pop("profissao")  # Remove e retorna o valor associado a "profissao"
5. Verificando Existência:

Você pode verificar se uma chave existe no dicionário.

Exemplo:

python
Copy code
if "cidade" in pessoa:
    print("Cidade:", pessoa["cidade"])
6. Iterando Sobre Chaves e Valores:

Utilizando loops, você pode iterar sobre as chaves ou os valores de um dicionário.

Exemplos:

python
Copy code
for chave in pessoa:
    print(chave, pessoa[chave])
python
Copy code
for chave, valor in pessoa.items():
    print(chave, valor)
7. Compreensão de Dicionário:

Uma maneira concisa de criar dicionários.

Exemplo:

python
Copy code
quadrados = {x: x**2 for x in range(5)}
8. Funções Relacionadas:

Métodos como get, setdefault, update e outros oferecem funcionalidades específicas.

Exemplo:

python
Copy code
valor = pessoa.get("altura", 0)  # Retorna 0 se "altura" não existir
Estes são conceitos fundamentais para trabalhar com dicionários em Python, que são uma implementação eficiente e flexível de estruturas de dados do tipo mapa.









"""

# Métodos de dicionários.




