"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, + min, max
"""
#         0      1        2    3    4
# lista = ['A', 'Bacana', 'C', 'D', 'E']
#
# string = 'ABacanaCDE'
#
# print(lista[1])
# print(string[1])
#
# lista[4] = 'ifce'
# print(lista)
# as listas assim como as "strings" suportam o fatiamento
# print(lista[0:3])

# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
#
# L1. extend(L2)
#
# L1.append('a')
# # append irá inserir algo no final da lista
# L1.insert(0, 'casa')
# # insert irá inserir algo no local desejado
#
# print(L1)
# print(L2)
# del(L2[1:3])
# # exclui elemento ou elementos desejados
# print(L2)
# # L3 = L1 + L2
# # print(L3)

# L4 = range(1, 10)
# print(L4)
#
# L4 = list(range(1, 10))
# # range cria uma espécie de lista compactada e o "list" descompacta
# print(L4)

palavra = 'ifce'
digitada = []
chance = 4

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Você digitou mais de uma letra.')
        continue

    digitada.append(letra)

    if letra in palavra:
        print(f'A letra "{letra}" existe na palavra secreta.')
        print()
    else:
        print(f'A letra "{letra}" não existe na palavra secreta')
        print()
        digitada.pop()

    palavra_temporaria = ''
    for letra_secreta in palavra:
        if letra_secreta in digitada:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '*'

    if palavra_temporaria == palavra:
        print(f'Você ganhou, a palavra era {palavra_temporaria}.')
        break

    else:
        print(f'A palavra secreta está assim: {palavra_temporaria}.')

    if letra not in palavra:
        chance -= 1
    print(f'Você ainda tem {chance} chances')
    print()
    if chance < 1:
        print('Você Perdeu!!!!!')
        break
