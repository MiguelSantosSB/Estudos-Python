'''
Argumentos nomeados e argumentos posicionais(não nomeados)
'''

def soma(x, y):
    print(f'{x=} e {y=}','|', x + y)
    # return x + y

soma(10, 5)
soma(y= 10, x= 5)
print(soma(10,5))
