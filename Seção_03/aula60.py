"""
Expressões Lambda(funções anônimas)
"""

# def funcao(arg, arg2):
#     return arg * arg2

# var = funcao(2,2)
# print(var)

# mesma coisa de:

# a = lambda x,y: x * y

# print(a(2,2))

lista = [
    ['P1', 22],
    ['P2', 66],
    ['P3', 4],
    ['P4', 33],
    ['P5', 20],
]
# irá receber o item e retornar na chave desejada
def func(item):
    return item[1]

# irá ordenar de acordo com a chave desejada
# do menor ao maior nesse caso 
# lista.sort(key = func)
# utilizando a lambda 
lista.sort(key = lambda item : item[1])


# nesse caso irá ser do meior para o menor 
# lista.sort(key = func, reverse = True)
print(lista)
