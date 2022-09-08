
variavel = 'valor'

def teste():
    print(variavel)

def teste2():
    variavel = 'outro'
# apesar de mudar o valor da variavel, dessa forma não irá mudar globalmente apenas dentro da função.
    print(variavel)

teste()
teste2()

print(variavel)
