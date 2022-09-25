"""
string = '012345678901234567890123456789012345678901234567890123456789'
tenho que gerar algo assim:
lista = ['0123456789', '0123456789', '0123456789']
e depois fazer isso:
retorno = '0123456789.0123456789.0123456789.0123456789.0123456789'
"""
# MINHA TENTATIVA:
string = '012345678901234567890123456789012345678901234567890123456789'

for i in range(0,len(string), 10):
    teste = [string[i:i+10]]
    teste = list(teste)

nova = teste[0:10]
a = 0
while a < 5:
    teste += nova
    a += 1

teste = '.'.join(teste)
print(teste)

