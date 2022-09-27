"""
Módulo
"""
import re

def removendo_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
# função que irá ser chamada para que retire qualquer coisa que não esteja entre 0 e 9, colocando '' no lugar 


def soma_da_multipliacacao(lista,multiplicador):
    resultado = []
    soma = 0
    for y, x in enumerate(lista):
        # resultado = []
        x = int(x)
        multiplicacao = x * multiplicador[y]
        resultado.append(multiplicacao)
        # resultado = sum(resultado)
    soma = sum(resultado)
    digit = 11 - (soma % 11)
    return digit
