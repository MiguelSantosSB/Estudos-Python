"""
Desempacotamento de listas
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5]

# n1, n2,*outra_lista, ultimo_da_lista = lista

# print(n1 , n2, outra_lista)
# luiz , joão , [maria, 1, 2, 3, 4, 5]
# print(ultimo_da_lista)
# 5

*outra_lista,n1, n2,  ultimo_da_lista = lista
print(n1, n2)
# 3 4
