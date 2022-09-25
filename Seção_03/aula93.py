"""
Problema dos Parâmetros Mutáveis em Funções
"""

def lista_de_clientes(cliente_iteravel, lista=None):
# como estavaantes :
# def lista_de_clientes(cliente_iteravel, lista=[]):
    if lista is None:
        lista = []
    lista.extend(cliente_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Bia'])
clientes2 = lista_de_clientes(['Matheus', 'Miguel', 'Samara'])
# Mutável: Lista, Dicionários
# Não-Mutável: Tuplas, strings, números, True, False, None

print(clientes1)
print(clientes2)
#  nesse caso por serem objetos mutáveis as 2 listas 
# estão se juntando e se transformando em 1 apenas
