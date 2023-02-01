'''
Escopo de funções e módulos em Python + global
'''
x =1 

def escopo():
    global x
    # Após colocar o global o 'x' irá ser mudado em todo código 
    x = 10

    def outro_escopo():
        global x
        x = 11
        y = 2

        print(x, y)
    outro_escopo()
    print(x)


print(x)
escopo()
print(x)