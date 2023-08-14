#Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.


pessoas = [('Hugo', 8),('Ana', 25), ('Gisele', 30),("Juliana", 45)]

def ordem_alfabetica(lista):
   pessoas_ordem_alfabetica = sorted(lista, key=lambda pessoa: pessoa[0])
   return pessoas_ordem_alfabetica

pessoas_alfabetica = ordem_alfabetica(pessoas)
print(pessoas_alfabetica)
