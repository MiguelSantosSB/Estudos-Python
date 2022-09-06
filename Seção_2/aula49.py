"""
CPF = 168.995.350-09
------------------------------------------------
1  *  10 = 10           #  1 *  11 = 11 
6  *  9  = 54           #  6  * 10  = 60
8  *  8  = 64           #  8  *  9  = 72 
9  *  7  = 63           #  9  *  8  = 72 
9  *  6  = 54           #  9  *  7  = 63
5  *  5  = 25           #  5  *  6  = 30
3  *  4  = 12           #  3  *  5  = 15
5  *  3  = 15           #  5  *  4  = 20 
0  *  2  = 0            #  0  *  3  = 0 
           297          #  0  *  2  = 0
                        #             343
11 - (297 % 11) = 11    #  11 - (343 % 11) = 9
11 > 9 = 0              #  digito 2 = 9
digito 1 = 0            #
"""


lista = '168995350'
resul = []
resul2 = []
a = list(range(10, 1, -1))
d = list(range(11, 1, -1))
mult = []
mult2 = []
result = 0
result2 = 0

for b, teste in enumerate(lista):
    teste = int(teste)
    resul = teste * a[b]
    mult.append(resul)
    result += mult[b]

digit1 = 11 - (result % 11) 

if digit1 > 9:
    soma = 0 
    lista = lista + str(soma)

for c, teste2 in enumerate(lista):
    teste2 = int(teste2)
    resul2 = teste2 * d[c]
    mult2.append(resul2)
    result2 += mult2[c]

digit2 = 11 - (result2 % 11)

if digit2 < 11:
    soma2 = 9
    lista = lista + str(soma2)

print(f'Seu Cpf completo e: {lista}')
