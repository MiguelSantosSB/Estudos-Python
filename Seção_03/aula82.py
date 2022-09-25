"""
Filter
"""
# utilizada para filtrar o que for pedido

from aula81dados import produto, pessoas, lista

# nova_lista = filter(lambda x: x > 5, lista)
# print(list(nova_lista))

# função que irá pegar os números da lista maiores que 5
def filtra(dado):
    if dado > 5:
        dado = True
        return True
# função que irá pegar os preços maiores que 50
def filtra2(dado):
    if dado['preco'] > 50:
        dado['certo'] = True
        return True
        
novo_dado = filter(filtra, lista)
novo_dado2 = filter(filtra2, produto)

# print(list(novo_dado))

# for novo_dado2 in novo_dado2:
    # print(novo_dado2)

