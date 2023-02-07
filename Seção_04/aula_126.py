'''
Sets em Python são mutáveis, porém aceitam apenas tipos 
imutáveis como: listas, dicionários e etc.

Representados graficamente pelo diagrama de Venn

    - Eficientes para remover valores duplicados(Seus valores serão sempre únicos)
    - Não garantem ordem
    - São iteráveis (for, in, not in)
'''
# Criando um Set
# set(iterável) ou {1,2,3}
# s1 = set()
# print(s1, type(s1))

s2 = {'ana clara',1,1,2,3,3,3,3,3,3,4,5}
# print(s2)

# print(3 in s2)
# for num in s2:
    # print(num)

# Métodos úteis :
# add, update, clear, discard

s1 = set()
# s1.add('ana')
s1.add(1)
s1.update(('olá mundo', 2, 3, 4))
# print(s1)
'''
Operadores úteis:

união | une
intersecção & itens presentes em ambos  
diferença - itens presentes apenas no set da esquerda
diferença simétrica ^ itens que não estão em ambos
'''

# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s1 ^ s2)

# Exemplos de uso de sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    print(letras)
