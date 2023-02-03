'''
Introdução ao tipo de dados dict - Dicionários em Python

    Dicionários são estruturas de dados do tipo par de 'chaves' e 'valor'.
'''

# ex de dicionário:
Pessoa = {
                'nome': 'Luiz Otavio',
                'Sobrenome': 'Miranda',
                'idade': 18,
                'altura': 1.82,
                'endereços': [
                    {'rua': 'bla bla bla', 'numero': 123},
                    {'rua': 'bla bla bla', 'numero': 12398}
                ]
            }

print(type(Pessoa))
print(Pessoa['endereços'])

print()

for chave in Pessoa:
    print(chave, Pessoa[chave])
    