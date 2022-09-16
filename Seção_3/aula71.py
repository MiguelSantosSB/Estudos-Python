"""
Geradores, Iteradores e Iteráveis
"""

# lista = [0,1,2,3,4,5]
# 'hasattr para saber se é um iterador
# print(hasattr(lista,'___next___'))

# transforma algo iteravel
# lista = iter(lista)

# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
import sys

lista = [x for x in range(10000)]
print(type(lista))
print(sys.getsizeof(lista))
# objetos geradores ocupa menos espaço e armazenam em grandes quantiades se necessário
lista = (x for x in range(10000))
print(type(lista))
<<<<<<< HEAD
# print(sys.getsizeof(lista))
=======
print(sys.getsizeof(lista))

# aaaaaa
>>>>>>> 615599f8b6d6a96c504b14f9d0fa6bbf269f78e9
