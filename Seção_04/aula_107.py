'''
Valores Padrão para parâmetros em funções
'''

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}','|', x + y + z)
    else:
        print(f'{x=} {y=}','|', x + y)

soma(5, 10, 2)

'''
Dessa forma vai ser errada pois o 0 será considerado como 'FALSE' logo não irá parar no if 
'''
def soma1(x, y, z=None):
    if z:
        print(f'{x=} {y=} {z=}','|', x + y + z)
    else:
        print(f'{x=} {y=}','|', x + y)

soma1(10,100,0)
