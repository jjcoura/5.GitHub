"""Programa desenvolvido para cadastro de clientes
em uma loja..."""
import defs
defs.limpaTerminal()

while True:
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
        print('\033[1;33mFINALIZANDO O PROGRAMA...\033[m')
    else:
        defs.limpaTerminal()
        defs.linha()
        print('\033[31mERRO! Favor inserir uma opção válida!\033[m')
        defs.linha()