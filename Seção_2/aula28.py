# isumeric ; isdigit ; isdecimal
# Podem receber apenas números positivos e inteiros

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
"""
print(num1.isnumeric())
print(num2.isnumeric())
# irá entragar um tipo booleano(true/false) se é ou não um número

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pode converter os números para realizar a conta.')
# O MAIOR problema dessa forma e que números com ponto flutuante(float) dão como errados
"""

try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except:
    print('ERROR')
