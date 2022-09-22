"""
Map - Dados
"""

from aula81dados import produto, pessoas, lista 

# print(lista)
# print(pessoas)
# print(produto)
# for teste in pessoas:
#     print(teste)

# nova_lista = [x  for x in lista]
# print(nova_lista)


# forma de pegar algo especifico de um dicionario usando o map eo lambda

nomes = map(lambda p: p['nome'], pessoas)

for nomes in nomes:
    print(nomes)
