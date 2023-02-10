'''
Exercício
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos pro deep copy (cópia profunda)
'''
produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 3', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]
'''
Ordene os produtos por nome decrescente (do maior para o menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

Ordene os produtos por preco crescente (do menor para o maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
'''
import copy
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')