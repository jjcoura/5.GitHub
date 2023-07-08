"""A função cadastro precisa conter:
# A função validar()
nome = validar.nome()
login = validar.login()
# Uma função para ler os logins
lerLogins = open('logins.txt', 'r')
um "FOR" para correr logins.readlines()
Se login for igual a valores[1].split() - cria uma lista
limpaTerminal() - limpa o Terminal
    senha    = validar.senha()
    email    = validar.email()
    data     = validar.data()
    telefone = validar.cel()
    endereço = validar.ed()
"""
import os

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def linha():
    return '-' * 32


def menu():
    print(' ======== <<< \033[1;36m "LOJA LEGAL" \033[m >>> ====== ')
    print('| \033[1;36m[1]\033[m \033[1;35m    -      Cadastrar Cliente    \033[m|')
    print('| \033[1;36m[2]\033[m \033[1;35m    -      Dados do Cliente     \033[m|')
    print('| \033[1;36m[3]\033[m \033[1;35m    -      Mostrar Clientes     \033[m|')
    print('| \033[1;36m[4]\033[m \033[1;35m    -      Gerar Relatório      \033[m|')
    print('| \033[1;36m[0]\033[m \033[1;35m    -      Sair                 \033[m|')
    linha()
    x = input('\033[1;36mDigite uma das opções acima: \033[m')
    linha()
    return x
    
    
def cadastro():
    limpaTerminal()
    print('=== < \033[1;92m        CADASTRAR USUÁRIO\033[m       > ===')