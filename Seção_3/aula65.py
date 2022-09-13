"""
-> e uma lista de listas de números inteiros
-> as listas internas tem o tamanho de 10 elementos  
-> as listas internas contém números entre 1 a 10 e eles podem ser duplicados 

exercício

-> Crie uma função que encontra o primeiro números duplicados considerando o 
    segundo número como a duplicação.
        Requisitos:
            a ordem dos números duplicados é considerada a partir da segunda 
            ocorrência( o número duplicado em si).
            exemplo: [ 1, 2, 3, ->3<- , 2, 1 ] -> 1,2 e 3 são duplicados
            se não encontrar duplicada na lista, retorne -1 
"""

from unicodedata import numeric


lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# for cont, teste  in enumerate(list(lista_de_listas_de_inteiros)):
#     print(lista_de_listas_de_inteiros[cont])

#     if teste[cont] == teste[cont]:
#         print('repetido')
#     else:
#         print('não repete')
  
# for a, teste in enumerate(lista_de_listas_de_inteiros):
#     print(a, teste)
#     print(teste[a][])

for num,teste in enumerate(lista_de_listas_de_inteiros):
    print(lista_de_listas_de_inteiros[num])
    for eh in teste:
        print(eh)
