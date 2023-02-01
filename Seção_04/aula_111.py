'''
*args para quantidade de argumentos não nomeados

    args - Argumentos não nomeados
    *args - (empacotamento e desempacotamento)
'''

# x, y, *resto = 1, 2, 3, 4

# print(x, y, resto)

# sum realiza a mesma coisa dessa fução
# print(sum((20, 10, 3, 2, 5)))

def soma(*args):
    total = 0   
    for numero in args:
        total += numero
    return total

teste1 = soma(1,2,3,4,5,6,76)
print(teste1)

# print(soma(1, 2, 10, 20, 7)) 
