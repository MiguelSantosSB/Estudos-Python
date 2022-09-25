"""
add(adicioan), update(atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apeas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
"""

# diferença entre os sets e as listas:
# eles(sets) só suportam elementos unicos, só recebem valores no caso
# eles não tem indice então não tem como acessar um valor especifico do set

set1 = {1,2,3,4,5}

# print(set1)

l1 = [1,2,3,4,5,6,6,6,6,6,6,6,7,8,9,'luiz','luiz']
# transforma em um set, removendo os elementos repetidos
l1 = set(l1)
print(l1)
# transforma de volta para lista e sem os itens repetidos
l1 = list(l1)
print(l1)

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}

s3 = s1 | s2
s4 = s2 - s1
s5 = s1 ^ s2 
s6 = s1 & s2

print(s3)
print(s4)
print(s5)
print(s6)
