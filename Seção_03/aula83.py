"""
Reduce
"""
from aula81dados import produto, pessoas, lista
from functools import reduce

# pegando a média dos produtos 
media_produtos = reduce(lambda ac ,p: p['preco' ] + ac, produto,0)
print(media_produtos / len(produto))
# 'ac' = acumulador/ onde vai ser alocado cada valor, sem modificação já que o ac e = 0  