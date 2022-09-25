"""
Funções Decoradoras e Decoradores
"""
#  funções decoradoras são funções que involvem outras funções, ou seja, uma função dentro de uma função

# def fala_oi():
#     print('oi')

# variavel = fala_oi
# variavel()

# def master():
#     def slave():
#         print('oi')
#     return slave()
# uma função que tem uma função escrava(função que precisa ser chamada para poder realizar o que for pedido)
# variavel = master()
# variavel()
# print(type(variavel))

# FUNÇÃO DECORADORA
def master(funcao):
    def slave():
        print('decorando...')
        funcao()
    return slave
# uma função que irá recebe outra função para realiza-la 

@master
# coloca a função dentro da função decoradora
def fala_oi():
    print('oi')

variavel = master(fala_oi)
# eh como se tivesse executando essa função diretamente
# variavel()
fala_oi()

