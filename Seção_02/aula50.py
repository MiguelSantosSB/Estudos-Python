from random import randint
cpf = str(randint(100000000, 999999999))

novo_cpf = cpf[0:9]

resul = []
resul2 = []
a = list(range(10, 1, -1))
d = list(range(11, 1, -1))
mult = []
mult2 = []
result = 0
result2 = 0

for b, teste in enumerate(novo_cpf):
    teste = int(teste)
    resul = teste * a[b]
    mult.append(resul)
    result += mult[b]

digit1 = 11 - (result % 11) 

if digit1 > 9:
    soma = 0 
    novo_cpf = novo_cpf + str(soma)

for c, teste2 in enumerate(novo_cpf):
    teste2 = int(teste2)
    resul2 = teste2 * d[c]
    mult2.append(resul2)
    result2 += mult2[c]

digit2 = 11 - (result2 % 11)

if digit2 < 11:
    soma2 = 9
    novo_cpf = novo_cpf + str(soma2)

if cpf == novo_cpf:
    print(f'cpf: {cpf}\nverificação do cpf: {novo_cpf}')
    print('Valido')
else:
    print(f'cpf: {cpf}\nverificação do cpf: {novo_cpf}')
    print('Invalido')
