'''
Closure e funções que retornam outras funções
'''

# def perfil(nome,idade,sexo,altura):
#     def pessoa():
#         return f'{nome}, {idade}, {sexo}, {altura}'
#     return pessoa


# pessoa1 = perfil('marcus', 32, 'm', 1.74)
# pessoa2 = perfil('maria', 26, 'f', 1.64)

# print(pessoa1())
# print(pessoa2())

def horario(horario):
    def pessoa(nome):
        return f'{horario}, {nome}'
    return pessoa

teste1 = horario('Bom Dia')
teste2 = horario('Boa Noite')

print(teste1('Miguel'))
print(teste2('Matheus'))

for name in ['Lucas', 'Davi', 'João']:
    print(teste1(name))
