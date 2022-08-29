"""
While em Python

x = 0
while x < 5:
    print(x)
    x = x + 1
# laço de repetição que irá se repetir até que a condição seja realizada
# 'while x < 5:' ---- condição
"""
"""
x = 0

while x < 10:
    y = 0
    while y < 5:

        print(f'({x},{y})')
        y += 1
    x += 1
"""

while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número!')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)

    escolha = input('Deseja continuar ? S/N')

    if escolha == 'S' or escolha == 's':
        continue
    elif escolha == 'N' or escolha == 'n':
        print('Desligando...')
        break
    elif not escolha == 'S' or not escolha == 's' or not escolha == 'N' or not escolha == 'n':
        print('Você não digitou nem "S" e nem "N", irá ser considerado como "N"')
