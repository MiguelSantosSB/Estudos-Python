"""
Uso de Try e Except como Condicional
"""

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
while True:

    numero = converte_numero(input('Digite um número: '))
    if numero is None:
        print('Error: isso não e um numero.')     
    else:
        print(numero * 2)

