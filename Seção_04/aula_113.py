'''

    Crie uma função que multiplique todos os argumentos não nomeados recebidos.
    Retorne o total para uma variavel e mostre o valor da variável.

    Crie uma função fala se um número é par ou ímpar.
    Retone se o número é par ou ímpar
'''

# Função multiplica args não nomeados

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

variavel = multiplica(2, 5, 3)
print(variavel)

# Função Par ou Ímpar 

def numero(x):
    if x % 2 == 0:
        return 'É Par'

    elif x % 2 == 1:
        return 'É Ímpar'

print(numero(13))
print(numero(12))