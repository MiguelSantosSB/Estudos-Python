"""
Funções - def 
"""

"""def funcao(msg, nome):
    print(msg, nome)

funcao('olá', 'João')
funcao('oi', 'Pedro')
funcao('Olá','Maria')
funcao('Coe','Ana')"""

def funcao(msg = 'olá', nome = 'Lucas'):
    return f'{msg} {nome}'

teste = funcao()
print(teste)
