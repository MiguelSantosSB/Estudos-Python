"""
Criando, Lendo, Escrevendo e Apagando Arquivos em Python
"""
# file = open('aula90.txt', 'w+')
# file.write('linha 1\n')
# file.write('linha 2\n')
# file.write('linha 3\n')
# #  escreve em um arquivo
# file.seek(0.0)
# # vai colocar o cursor para o topo para que possa acontecer a leitura
# print(file.read())
# # file.read vai ler o arquivo onde o cursor estiver
# file.close()
# # vai fechar o arquivo por não ter mais nenhuma finalidade dele aberto

# MELHOR MANEIRA DE SE TRABALHAR COM ARQUIVO

# CRIANDO O ARQUIVO .TXT(SE O ARQUIVO JÁ FOR EXISTENTE OS DADOS DELE IRAM SER APAGADOS E SUBSTITUIDOS)
# with open('aula90.txt', 'w+') as file:
#     file.write('linha 1\n')
#     file.write('linha 2\n')
#     file.write('linha 3\n')

#     file.seek(0.0)
#     print(file.read())

# # ACRESCENTANDO COISAS NO ARQUIVO .TXT
# with open('aula90.txt', 'a+') as file:
#     file.write('outra linha\n')
    
#     file.seek(0.0)
#     print(file.read())

# APENAS LENDO O ARQUIVO .TXT
# with open('aula90.txt', 'r+') as file:
#     print(file.read())

