"""
Manipulando Strings

- String Indices
- Fatiamento de Strings
- Funções built-in, abs, type, print, etc...
"""

palavra = 'ifce'

print(palavra[2])
# vai buscar a letra pertencente a posoção '2' nesse caso

nova_palavra = palavra[2:4]
print(nova_palavra)
# fatiamento de string
# cria uma nova string, retirada de outra string(uma fatia de outra sting)

nov_palavra = palavra[0::2]
print(nov_palavra)
# fatia a string pulando as letras de acordo como pedido
