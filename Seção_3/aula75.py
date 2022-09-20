"""
Zip e Zip_longest

Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Fortaleza']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)

print(list(cidades_estados))
# o Zip une 2 litas.
# se as listas não forem iguais a menor lista irá determinar o tamanho do zip

cidades_estados = zip_longest(cidades, estados, fillvalue='estado')
print(list(cidades_estados))

# no caso do Zip_longest o limitador dele e a maior lista
# para utilizar esse zip e preciso importar 
# e no caso de uma lista menor será adicionado 'None' nos espaços em falta
# podendo ser substituido o 'None' por qualquer coisa com a função: 'fillvalue'= "palavra escolhida" 
