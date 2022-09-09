perguntas = {
    'pergunta1' : {
        'pergunta' : 'Quanto é 2 + 2 ?',
        'resposta' : {
            'a' : '1',
            'b' : '4',
            'c' : '6',
            'd' : '5', 
        },
        'resposta_certa' : 'b'
    },
    'pergunta2' : {
        'pergunta' : 'Quanto é 2 * 2 ?',
        'resposta' : {
            'a' : '6',
            'b' : '2',
            'c' : '4',
            'd' : '8', 
        },
        'resposta_certa' : 'c'
    },
    'pergunta3' : {
        'pergunta' : 'Quanto é 2 / 2 ?',
        'resposta' : {
            'a' : '1',
            'b' : '2',
            'c' : '-2',
            'd' : '0', 
        },
        'resposta_certa' : 'a'
    },
}

resp_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['resposta'].items():
        print(f'[{rk}]: {rv}')

    resp = input()
    if resp == pv['resposta_certa']:
        print('ACERTOUUUU')
        resp_certas += 1 
    else:
        print('ERROOOOOU')
    
    print(f'{resp_certas}')
