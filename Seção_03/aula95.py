"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
import aula95_2

cnpj = '04.252.011/0001-10'
novo_cnpj = list(aula95_2.removendo_caracteres(cnpj))
    # preciso tirar os "." ,  "/" e "-"
    # depois tirar os 2 ultimos números
del novo_cnpj[13]
del novo_cnpj[12]
    # excluindo o 2 ultimos números

teste1 = list(range(5,1,-1)) + list(range(9,1,-1))

b = aula95_2.soma_da_multipliacacao(novo_cnpj, teste1)

if b > 9:
    novo_digito = 0
    novo_digito = str(novo_digito)
    novo_cnpj.append(novo_digito)

else:
    novo_digito = b
    novo_digito = str(novo_digito)
    novo_cnpj.append(novo_digito)

teste1.insert(0,6)

a = aula95_2.soma_da_multipliacacao(novo_cnpj, teste1)

if a > 9:
    novo_digito = 0
    novo_digito = str(novo_digito)
    novo_cnpj.append(novo_digito)

else:
    novo_digito = a
    novo_digito = str(novo_digito)
    novo_cnpj.append(novo_digito)

cnpj = list(aula95_2.removendo_caracteres(cnpj))
if novo_cnpj == cnpj:
    print('Este cnpj e valido!')
    print(f'Cnpj dado: {cnpj}')
    print(f'Cnpj validado: {novo_cnpj}')

else: 
    print('Este cnpj não e valido!')
    print(f'Cnpj dado: {cnpj}')
    print(f'Cnpj validado: {novo_cnpj}')
