"""
Groupby - Agrupando valores
"""
from itertools import groupby
# para poder utilizar do groupby e necessario ordenar o dicionario.

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
# organizando o dicionario pelas notas
alunos_agrupados = groupby(alunos, ordena)

for grupo, valores  in alunos_agrupados:
    print(f'Agrupamento: {grupo}')
    # grupo vai ser o referencial para separar os alunos
    for aluno in valores:
        print(aluno)
        