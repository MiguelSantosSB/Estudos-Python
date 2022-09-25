"""
Split, Join e Enumerate em Python
-- Split - Divide uma string 
-- join - Junta uma lista
-- Enumerate - Enumera elementos da lista
"""

str = 'bom dia, que dia e hoje?'
# lista1 = str.split(' ')
# # separa a string pelos espaços
# lista2 = str.split(',')
# separa a string pela virgula 

"""
print(lista1)
print()
print(lista2)
"""
# uma forma mais facil de apresentar a lista
"""for valor in lista1:
    print(valor)

print()

for valor in lista2:
    print(valor)"""


lista = str.split(' ')
str2 = ' '.join(lista)

# print(str)
# print(lista)
# print(str2)

# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])
# valor e lista[indice] são a mesma coisa nesse caso
