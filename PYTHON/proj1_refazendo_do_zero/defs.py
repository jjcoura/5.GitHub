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
    
    
    
def cadastro():
    limpaTerminal()
    print('=== < \033[1;92m        CADASTRAR USUÁRIO\033[m       > ===')