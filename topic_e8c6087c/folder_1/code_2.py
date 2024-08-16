from folder1_2 import *

'''
O folder1_2/__init__.py indica a importação de apenas duas variaveis
Entao code1_var_c nao é reconhecida neste contexto.
'''
print(code1_var_a)
print(code1_var_b)
# Se retirar o comentario da linha a seguir gera erro.
# A variável não é conhecida. Pois nao esta importada pelo folder1_2/__init__.py
#print(code1_var_c)
