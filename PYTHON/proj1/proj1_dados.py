"""Crie um programa que faça o cadastro de clientes e salve os dados 
e ainda seja possivel gerar um relatório final."""

import defs

defs.limpaterminal()

escolha = defs.menu()

if escolha == '1':
    defs.cadastro()
elif escolha == '2':
    defs.mostrarDados()
elif escolha == '3':
    defs.clientesCadastrados()
elif escolha == '4':
    defs.relatorio()
elif escolha == '0':
    print('\033[1;36mFINALIZANDO O PROGRAMA...\033[m')
else:
    defs.limpaTerminal()
    defs.criaBarra()
    print('\033[1;31m"Favor inserir uma opção válida!"\033[m')
    defs.criaBarra()
