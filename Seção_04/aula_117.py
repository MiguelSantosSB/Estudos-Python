'''
#Exercícios

    Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
'''

def duplicar(num):
    return 2 * num

# print(duplicar(10))

def multiplicador(multiplica):
    def multiplicando(numero):
        return multiplica * numero
    return multiplicando

teste = multiplicador(100)

print(teste(10))