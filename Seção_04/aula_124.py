# Exercício - Sistema de perguntas e respostas

perguntas = [

    {
        'Pergunta': 'Quanto e 2 + 2 ?',
        'Opções': ['2','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto e 5 * 5 ?',
        'Opções': ['10','25','46','50'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto e 10 / 2 ?',
        'Opções': ['4','2','20','5'],
        'Resposta': '5',
    },
]
resposta = perguntas

acertos = 0
for pergunta in perguntas:
    print('Pergunta: ',pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for num, opcao  in enumerate(opcoes):
        print(f'{num})',opcao)
    print()

    response = input()

    acertou = False
    response_int = None
    qtd_opcoes = len(opcoes)

    if response.isdigit():
        response_int = int(response)

    if response_int is not None:
        if response_int >= 0 and response_int < qtd_opcoes:
                if opcoes[response_int] == pergunta['Resposta']:
                    acertou = True
    
    print()
    if acertou:
        print('Você acertou')
        acertos += 1
    else:
        print('Você errou')
        print()

print(f'Você teve um total de {acertos} acertos')
print('de', num, 'perguntas')
