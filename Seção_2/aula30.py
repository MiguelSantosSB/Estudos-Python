"""
# 1o
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.


num = input('Digite um número inteiro: ')

inteiro = num.isnumeric()

try:
    num = int(num)
    if inteiro == True or num < 0:
        if num % 2 == 0:
            print('Seu número e Par!')
        elif num % 1 == 0:
            print('Seu número e Ímpar!')
except:
    print('Seu número não e inteiro!')
# perguntar depois a questão dos números negativos
"""

# ------------------------------------------------------------------------------

# 2o
# Faça um programa que pergunte a hora ao usuário e,baseando-se no horário
# descrito, exiba a saudação apropriada.

"""
hora = input('Digite a atual hora: ')

existe = hora.isnumeric()

try:
    hora = int(hora)
    if existe == True:
        if hora >= 0 and 11 >= hora:
            print('Bom dia!')
        elif hora >= 12 and 17 >= hora:
            print('Boa tarde!')
        elif hora >= 18 and 23 >= hora:
            print('Boa noite!')
        else:
            print('Valor digitado não existe uma hora correspondente ')
except:
    print('O valor digitado não é um número natural')
"""

# ------------------------------------------------------------------------------

"""
# 3o
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
# menos escreva "seu nome é curto"; se tiver entre 5 e 6 letra, escreva 
# "seu nome é normal";maior que 6 escreva "seu nome é muito grande"


nome = input('Digite seu primeiro nome: ')
letras = len(nome)

if letras <= 4:
    print('Seu nome é muito curto')
elif letras >= 5 and 6 >= letras:
    print('Seu nome é normal')
elif letras > 6:
    print('Seu nome é muito grande')
"""
