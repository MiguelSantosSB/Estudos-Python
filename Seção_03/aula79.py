"""
Combinations, Permutations e Product 
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['maicon','pedro', 'michael', 'maria', 'amanda']

for grupo in combinations(pessoas, 2):
    print(grupo)
# irá combinar o grupo 'pessoas' em pares de acordo como pedido, se importando com a ordem
# ou seja, não ocorrerá de ter: ('maicon','pedro') e ('pedro','maicon'), não existirar: ('maicon','maicon')
print('#' * 80)

for grupo in permutations(pessoas, 2):
    print(grupo)
# irá combinar o grupo 'pessoas' em pares de acordo como pedido, sem se importar com a ordem
# ou seja, poderá ocorrer de ter: ('maicon','pedro') e ('pedro','maicon'), não existirar: ('maicon','maicon')
print('#' * 80)

for grupo in product(pessoas, repeat=2):
    print(grupo)
# irá combinar o grupo 'pessoas', sem se importar com a ordem
# ou seja, poderá ocorrer de ter: ('maicon','pedro') e ('pedro','maicon')
# existirar: ('maicon','maicon') de acordo como pedido no 'repeat'
print('#' * 80)

