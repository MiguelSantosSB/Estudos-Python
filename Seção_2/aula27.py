# Quantidade de caracteres
"""
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

#print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Quantidade de caracteres muito baixo!')
else:
    print('Quantidade de caracteres boa')
"""

# Soma da quantidade de caracteres de 2 paralavras

str1 = input('Digite uma palavra: ')
str2 = input('Digite outra palavra: ')

print(f'A quantidade de caracteres digitados e: {len(str1) + len(str2)}')
