"""
Módulo padrão do Python
Módulos são arquivos .py (que contém  código python) e servem para expandir
as funcionalidades padrão da linguagem.
"""
# import sys 
# print(sys.platform)

from sys import platform
print(platform)

from random import randint as aleatorio
for i in range(10):
    print(aleatorio(0,10))
