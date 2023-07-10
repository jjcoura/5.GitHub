"""Programa desenvolvido para cadastro de clientes
em uma loja..."""
from defs import *
from valida import *


escolha = menu() 
if escolha == '1':
    cadastro() 
elif escolha == '2':
    mostrarDados()
elif escolha == ''