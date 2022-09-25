"""
Faça uma lista de tarefascom as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a ultima ação)
    opção de refazer (a cada vez que chamarmos, refaz aultima ação)
"""

def adiciona(recebe, lista):
    lista.append(recebe)

def listar(lista):
    print(lista)

def desfazer(lista,reserva):
    lista_desfazer = lista.pop()
    reserva.append(lista_desfazer)

def refazer(lista, reserva):
    lista_refazer = reserva.pop()
    lista.append(lista_refazer)


lista_tarefas = []
lista_reserva = []

continua = 's'

while continua != 'n':

    escolha = input('O que deseja fazer ? 1- adicionar // 2- listar // 3- desfazer // 4- refazerz\n')

    if escolha == '1':
        palavra = input('')
        adiciona(palavra, lista_tarefas)

    elif escolha == '2':
        listar(lista_tarefas)

    elif escolha == '3':
        desfazer(lista_tarefas, lista_reserva)

    elif escolha == '4':        
        refazer(lista_tarefas, lista_reserva)

    continua = input('Deseja continuar ? s/n ')
# tentei fazer do meu jeito mas tive dificuldades com a parte de executar a lógica provavelmente 
# vi a solução porém só me "inspirei" nela
