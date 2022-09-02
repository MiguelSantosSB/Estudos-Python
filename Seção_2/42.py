"""
Enumerate - enumerar elementos da lista
"""
lista = [ 
   #   0       1       2 
    ['Edu', 'João', 'Luiz'],       # 0
    ['Mariana', 'Aline', 'Joana'], # 1
    ['Helena', 'Davi', 'Mad']      # 2
]
enumerada = list(enumerate(lista))
# print(enumerada[0][1][2])

for v1, v2 in enumerate(lista):
    print(v1, v2)
