# ctrl + / para comentar de forma rapida
"""
Iteração de strings com o uso do while
"""

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_frase = ''

# while contador < tamanho_frase:
#
#     nova_frase += frase[contador]
#     print(nova_frase)
#     contador += 1
# print(nova_frase)

# copiar uma string para outra vazia

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_frase += 'R'
    else:
        nova_frase += letra
    contador += 1

print(nova_frase)

# faz com que determinado caractere escolhido mude ou fique maiusculo
