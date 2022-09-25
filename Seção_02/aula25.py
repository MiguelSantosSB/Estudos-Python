"""
Operadores Relacionais
== ; > ; >= ; < ; <= ; !=
"""
"""
print(2 == 2)

num1 = 2 # int
num2 = '2' # str
num3 = 2

print(num1 == num2)

print(num1 < num3)

print(num1 <= num3)

print(num1 > num3)

print(num1 >= num3)
"""

nome = input('Qual seu nome ?')
idade = int(input('Digite sua idade'))
limiteMin = 20
limiteMax = 30

if idade >= limiteMin and idade <= limiteMax:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} não pode pegar o emprestimo')
