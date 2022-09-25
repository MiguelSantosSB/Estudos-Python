"""
Operadores Lógicos
and ; or ; not ; in ; not in
"""

# AND
# Verdadeiro E Verdadeiro
# comparacap1 and comparacao2

# OR
# Verdadeiro OU Verdaderio
# comparacao1 or comparacao2

# Not
"""
a = ''
# Se 'a' não tem nenhum valor
if not a:
    print('preencha o valor de a.')

# IN
nome = 'miguel'

if 'm' in nome:
    print('Existe M')
else:
    print('Não existe')
"""
# Sistema Simples de usuario e senha
nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

nome_dados = 'miguel'
senha_dados = '1234'

if nome_dados == nome and senha_dados == senha:
    print('Acesso liberado!')
else:
    print('Acesso negado')


