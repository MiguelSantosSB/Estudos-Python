"""
while / Else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break
# quando o contador passar de '5' ele irá direto para o print depois do else
# assim chegando a nem passar pelo else

    acumulador = acumulador + contador
    contador += 1
else:
    print('eh isso')
print('Não eh isso')
