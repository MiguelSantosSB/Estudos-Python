"""
Funções (def) - *args **kwargs -
"""

def teste(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')
    print(idade)
    print(kwargs['nome'])

    # print(args[0])
    # print(*args)
lista = [1,2,3,4,5]
# teste(1,2,3,4,5)
teste(*lista, nome = 'miguel', idade = 31)
