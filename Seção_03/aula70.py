"""
Dictionary Comprehension
"""
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x: y for x, y in lista}
# mesma coisa porém usando uma função especifica
# d1 = dict(lista)
print(d1)

d1 = {x: y*2 for x, y in lista}
print(d1)

d1 = {x: y for x, y in enumerate(range(5))}
print(d1)
