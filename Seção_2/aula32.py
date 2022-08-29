"""
Formatar valores com modificadores

:s - Texto (string)
:d - Inteiro (int)
:f - Ponto flutuante (float)
:. - Quantidade de casas decimais de um float

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
sub = num1 / num2
# formas de se delimitar o número de casas decimais
print(sub)
print(f'{sub:.2f}')
print('{:.4f}'.format(sub))

num4 = 1
print(f'{num4:0>10}')
# '0>10' eu digo que o número tem o total de 10 casas
# como o num4 n tem esse tamanho então e colocado o '0' no lugar

print(f'{num4:0<10}')

nome = 'miguel'

print(f'{nome:#^10}')
print(f'{nome:#>10}')
print(f'{nome:#<10}')
