
nome = 'miguel'
idade = 20
e_maior = idade > 18
peso = 90
altura = 1.71
imc = peso / altura ** 2


print(f'{nome} tem {idade} anos de idade e seu imc e: {imc}')

print(f'{nome} tem {idade} anos de idade e seu imc e: {imc:.2f}')

print('{0} tem {1} anos de idade e seu imc e: {2}'.format(nome, idade, imc))

print('{0} tem {1} {0} anos de idade e seu imc e: {2}'.format(nome, idade, imc))
