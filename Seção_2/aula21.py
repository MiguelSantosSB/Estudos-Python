nome = 'miguel'
altura = 1.71
peso = 98.60
imc = peso / altura ** 2
ano_at = 2022
idade = 20
nascimento = ano_at - idade

print(f'{nome} tem {idade} anos, {altura} de altura e {peso}kg de peso.')
print(f'O Imc de {nome} e {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
