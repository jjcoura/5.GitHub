"""Programa desenvolvido para cadastro de clientes
em uma loja..."""
from defs import *
print(menu())
escolha = menu() # a função menu é que vai gerenciar as escolhas.
if escolha == '1':
    cadastro() # bom aqui começa a função cadastro