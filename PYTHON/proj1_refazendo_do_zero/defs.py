import os
from datetime import datetime
from valida import *

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def linha():
    return '-' * 32

data = datetime.now()
dia = data.day
mes = data.month
ano = data.year

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
    u_nome = nome()
    u_login = login()
    with open('logins.txt', 'r') as lerlogins:
        for l in lerlogins.readlines():
            valores = l.split('-')
            if u_login == valores[1].split(':')[1].strip():
                limpaTerminal()
                linha()
                print('\033[31mLogin Existente!\033[m')
                linha()
                return
    u_senha = senha()
    u_email = email()
    u_dia, u_mes, u_ano = nascimento()
    u_data = f'{u_dia}/{u_mes}/{u_ano}'
    u_cel = cel()
    u_endereco = endereco()
    limpaTerminal()
    linha()
    print('Cliente cadastrado com sucesso!')
    linha()
    with open('logins.txt', 'a') as logins:
        logins.write(f'Nome: {u_nome} - Login: {u_login} - Senha: {u_senha} - Email: {u_email} - Data de nascimento: {u_data} - Número de celular: {u_cel} - Endereço: {u_endereco}\n')


def mostrarDados():
    limpaTerminal()
    print('=== < \033[1;92m        DADOS DO CLIENTE\033[m       > ===')
    linha()
    logins = open('logins.txt', 'r')
    for l in logins.readlines():
        valores = l.split('-')
        limpaTerminal()
        linha()
        print('\033[1;32mCliente Logado! Dados do usuário:\033[m')
        linha()
        for p in range(len(valores)):
            if valores[p].split(':')[0] == 'Endereço':
                dictEndereco = eval(valores[p].split('Endereço: ')[1])
                for chave, valor in dictEndereco.items():
                    print(f'{chave}: {valor}')
            else:
                print(valores[p])
        linha()
    logins.close()
    
    
def senha():
    while True:
        print('Digite uma senha com seis dígitos!')
        print('Conselho: "evite datas de aniversário ou senhas sequenciais".')
        senha = input('Senha: ')
        if senha == '':
            print('\033[31mErro! Senha indefinida! Favor digitar uma senha válida!\033[m')
        elif len(senha) != 6:
            print('\033[31mErro! A senha deve conter exatamente seis dígitos!\033[m')
        else:
            return senha        
        

def clientesCadastrados():
    limpaTerminal()
    print('=== < \033[1;92m        CLIENTES CADASTRADOS\033[m       > ===')
    logins = open('logins.txt', 'r')
    for l in logins.readlines():
        l = l.strip()
        print(f'\033[1;92m{l}\033[m')
    logins.close()
    linha()

def relatorio():
    cc = 0
    nomess = []
    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0].split(':')[1].strip())
        cc += 1
    logins.close()
    limpaTerminal()
    arquivo = open('dados.txt', 'w+')
    arquivo.write('Relatório de Clientes\n')
    arquivo.write('\n')
    arquivo.write(f'A loja legal possui {cc} cliente(s)\n')
    arquivo.write('\n')
    for i in range(len(nomess)):
        arquivo.write(f'{i + 1}. {nomess[i]}\n')
    arquivo.write(f'Brasil, {dia}/{mes}/{ano}.\n')
    arquivo.close()
    linha()
    print('\033[1;32mRelatório gerado em "dados.txt"\033[m')
    linha()


def verifica_arquivo_logins():
    if not os.path.exists('logins.txt'):
        with open('logins.txt', 'w') as arquivo:
            arquivo.write('')

