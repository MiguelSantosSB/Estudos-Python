"""
Levantando Exceções em Python(raise)
"""

def divide(n1,n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser "0".')
    return n1/n2

# print(divide(2, 0))
# dessa forma foi criado um parametro de erro 
# que quando o if for True, o erro será aplicado.

try:
    print(divide(2, 0))
except ValueError as error:
    print('Você está tentando dividir por "0"')
    print('Log:', error)

