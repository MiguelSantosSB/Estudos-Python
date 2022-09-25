carrinho = []

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 50))

teste = [(y) for x, y in carrinho]
teste = sum(list(teste))
print(teste)

