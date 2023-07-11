"""Crie um programa que faça o cadastro de clientes e salve os dados 
e ainda seja possivel gerar um relatório final."""

from defs import *
limpaTerminal()
verifica_arquivo_logins()

while True:
    escolha = menu()

    if escolha == '1':
        cadastro()
    elif escolha == '2':
        mostrarDados()
    elif escolha == '3':
        clientesCadastrados()
    elif escolha == '4':
        relatorio()
    elif escolha == '0':
        break
        print('\033[1;36mFINALIZANDO O PROGRAMA...\033[m')
    else:
        limpaTerminal()
        linha()
        print('\033[1;31m"Favor inserir uma opção válida!"\033[m')
        linha()
