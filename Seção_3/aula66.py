"""
List Comprehension
"""

lista1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in lista1]
# print(ex1)

ex2 = [variavel * 2 for variavel in lista1]
# print(ex2)

ex3 = [(variavel,variavel2) for variavel in lista1 for variavel2 in range(3)]
# print(ex3)


# upper - deixa as letras maiúsculas 
# replace - irá substituir a letra 'a' por '@'
lista2 = ['luiz', 'mauro', 'lais']
ex4 = [v.replace('a','@').upper() for v in lista2]
# print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

ex5 = [(x, y) for x, y in tupla]
# print(ex5)
ex5 = dict(ex5)
# print(ex5)

lista3 = range(100)
# vai buscar os números divisiveis por 3 e por 8 
ex6 = [v for v in lista3 if v % 3 == 0 if v % 8 == 0]
# print(ex6)


