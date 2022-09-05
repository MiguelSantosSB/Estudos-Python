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

# num1 = int(lista[0])
# num1 = num1 * 10
# print(num1)
# for c, teste in enumerate(lista):
#     list = []   
#     list.append(teste)
#     print(list[1])


a = list(range(10, 1, -1))
d = list(range(11, 1, -1))
mult = []
result = 0

for b, teste in enumerate(lista):
    teste = int(teste)
    resul = teste * a[b]
    mult.append(resul)
    # print(f'{teste} * {c[b]} = {resul}')
    result += mult[b]
    # print(mult)
    # print(result)

# print(f'{result}')
digit1 = 11 - (result % 11) 
# print(digit1)


if digit1 > 9:
    soma = 0 
    lista = lista + str(soma)
    print(lista)

for c, teste2 in enumerate(lista):
    teste2 = int(teste2)
    resul2 = teste2 * c[d]
    mult.append(resul2)
    print(f'{teste2} * {d[c]} = {resul2}')
    result += mult[c]
    
