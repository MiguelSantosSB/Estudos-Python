"""
Exercicío
    Crie uma função que encontra o primeiro duplicado considerando o segundo número como a duplicação.
    Retorne a duplicação considerada.
    Requisitos:
        A ordem do número duplicado e considerada a partir da segunda ocorrência do número, ou seja, o 
        número duplicado em si.
        Exemplo:
            [1,2,3,3,2,1] -> 1,2 e 3 são duplicados(retorne 3) 
            [1,2,3,4,5,6] -> retorne -1 (não tem duplicados)
"""

lista = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,7,7,3,1,9],
    [4,8,8,8,5,1,10,3,1,7],
    [1,3,7,2,2,1,5,1,9,9],
    [10,2,2,1,3,5,10,5,10,1],
    # [1,2,3,4,5,6,7,8,9,10],
]

# def encontra_primeiro_duplicado(lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1

#     for numero in lista_de_inteiros:
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break

#         numeros_checados.add(numero)

#     return primeiro_duplicado


# for lista1 in lista:
#     print(
#         lista1,
#         encontra_primeiro_duplicado(lista1)
#     )
# ---------------------------------------------------------------------------



def teste_t(lista_para_teste):
    ordem = range(10)
    numeros_checados = set()
    primeiro_duplicado = -1

    for digit in ordem:
        for list in lista_para_teste:
            if list in numeros_checados:
                primeiro_duplicado = list[digit]
                # print(primeiro_duplicado)
                break        
            numeros_checados.add(list)

            return primeiro_duplicado

for teste in lista:
    print(teste, teste_t(teste))