"""
Criar uma função zipper
O trabalho dessa função será unir duas listas na ordem.
ex: 
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
"""
estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']
lista = []

for zippe in zip(estados, siglas):
    lista.append(zippe)
    print(zippe)

print(lista)