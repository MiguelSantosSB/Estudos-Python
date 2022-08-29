"""
For
for com stings
função range(start=0; stop; step=1)
"""

# texto = 'Python'
#
# for n , letra in enumerate(texto):
#     print(n, letra)
# Função enumerate numera cada volta do laço de repetição(FOR)

# for numero in range(10):
#     print(numero)

# for numero in range(10):
#     print(numero)
# range( inicia em , para no , vai de quantos em quantos)

texto = 'python'
novo_texto = ''

for letra in texto:
    if letra == 't':
        novo_texto = novo_texto + letra.upper()
    elif letra == 'h':
        novo_texto += letra.upper()
        break
    else:
        novo_texto += letra
print(novo_texto)
