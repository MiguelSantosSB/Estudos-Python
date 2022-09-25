"""
Dicionário em Python
"""

d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'valor da nova chave'

# print(d1['chave1'])

d2 = {
    'str' : 'valor',
    123: 'outro valor',
    (1,2,3,4) : 'Tupla'
}

# print(d2['str'])
# print(d2[123])
# print(d2[(1,2,3,4)])

# adiciona algo no dicionário 
# d2.update({'chave':'ehhhh'})

# if d2.get('chave') is not None:
#     print(d2.get('chave'))
# print(d2['chave'])

# del d2[123]

# print(d2)

# verifica se o que está entre aspas está presente no dicionário
# print('str' in d2.keys())

# verifica se o que está entre aspas está presente nos valores dentro do dicionário 
# print('valor' in d2.values())

# -------------------------------------------------------------------------------------------------------------------

# somando um dicionario com outro

d1.update(d2)
# print(d1)
