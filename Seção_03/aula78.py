"""
Count - contadores infinitos
"""

from itertools import count
# preciso importar para usar o count

contador = count(start = 0, step = 1)
# start = de onde quer começar
# step = de quanto em quanto eu quero que pule

for teste in contador:
    print(teste)
    if teste == 10:
        break

