"""
For / Else em Python
"""
var = ['ifce', 'joao', 'fortal']

comeca_com_j = False
for valor in var:
    if valor.startswith('j'):
        comeca_com_j = True
if comeca_com_j:
    print('Existe uma palavra que começa com j.')
else:
    print('Não existe uma palavra que começa com j.')

"""
 if valor.startswith('j'):
   print('Começa com "j"', valor)
 else:
    print('Não começa com "j"', valor)
 """

