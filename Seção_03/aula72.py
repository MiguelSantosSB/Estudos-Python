"""
Comportamento de geradores e iteradores
"""
nome = 'miguel santos'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print('for agora')
for letra in gerador:
    print(letra)
print(next(gerador)) #da mesma forma dos iteradores o gerador também irá
# dar erro quando o valor for consumido 

# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
# print(next(iterador)) # aqui foi consumido por completo o iterador  
# print(next(iterador)) # aqui irá da erro por não ter mais o que consumir 
