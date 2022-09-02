"""
Operador ternário 
"""
# Sem o operador ternário:
login_user = True

if login_user == True:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar'

print(msg)

# A mesma coisa:

# Com o operador ternário:
msg = 'Usuário logado.' if login_user else 'Usuário precisa logar.'

print(msg)





