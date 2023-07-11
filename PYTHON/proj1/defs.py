from validar import *
from datetime import datetime
import os

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


# definições: Cadastrar, Checar login existente, adicionar dados no arquivo txt
def cadastro():
    limpaTerminal()
    print('=== < \033[1;92m        CADASTRAR USUÁRIO\033[m       > ===')
    onome = nome()
    ologin = login()
    with open('logins.txt', 'r') as lerlogins:
        for l in lerlogins.readlines():
            valores = l.split('-')
            if ologin == valores[1].split(':')[1].strip():
                limpaTerminal()
                linha()
                print('\033[31mLogin Existente!\033[m')
                linha()
                return
    osenha = senha()
    oemail = email()
    odia, omes, oano = datas()
    odia = f'{odia}/{omes}/{oano}'
    ocel = cel()
    oed = ed()
    limpaTerminal()
    linha()
    print('\033[1;32mCLIENTE CADASTRADO COM SUCESSO!\033[m')
    linha()
    with open('logins.txt', 'a') as logins:
        logins.write(f'Nome: {onome} - Login: {ologin} - Senha: {osenha} - Email: {oemail}'
                     f'- Data de Nascimento: {odia} - Número de celular: {ocel} - '
                     f'Endereço: {oed}\n')


def mostrarDados():
    limpaTerminal()
    print('=== < \033[1;92m        DADOS DO CLIENTE\033[m       > ===')
    print()
    print('\033[1;31mlogue para acessar os seus dados!\033[m ')
    print()
    userlogin = input('Login: ')
    usersenha = input('Senha: ')
    validar = False
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        valores = linha.split('-')
        if userlogin == valores[1].split(':')[1].strip and usersenha == valores[2].split(':')[1].strip():
            limpaTerminal()
            linha()
            print('\033[1;32mCliente Logado! Dados do usuário:\033[m')
            linha()
            for percorre in range(len(valores)):
                if valores[percorre].split(':')[0] == 'Endereço':
                    dictEndereço = eval(valores[percorre].split('Endereço: ')[1])
                    for chave in dictEndereço.items():
                        print(f'{chave} : {valor}')
                else:
                    print(valores[percorre])
            linha()
            validar = True
            break
    logins.close()
    if not validar:
        limpaTerminal()
        print('-' * 32)
        print('\033[1;31mERRO! logoin ou senha inválidos!\033[m')
        print ( '-' * 32 )
        

 # exibir todos os clientes já cadastrados       
def clientesCadastrados(): 
    limpaTerminal()
    print('=== < \033[1;92m        CLIENTES CADASTRADOS\033[m       > ===')   
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        l = linha.split('-')
        print(f'\033[1;92m]{l[0]} | {l[1]}\033[m')
    logins.close()
    print('-' * 32)


def verifica_arquivo_logins() :
    if not os.path.exists ( 'logins.txt' ) :
         with open ( 'logins.txt', 'w' ) as arquivo :
            arquivo.write ( '' )


def relatorio():
    countClient = 0 
    nomess = []
    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0].split(':')[1].strip())
        countClient += 1
    logins.close()
    limpaTerminal()
    arquivo = open('dados.txt', 'w+')
    arquivo.write('Relatório de Clientes\n')
    arquivo.write(f'A loja LEGAL possui {countClient} clientes(s)\n')
    for i in range(len(nomess)):
        arquivo.write(str(f'{i + 1}.{nomess[i]}\n'))
    arquivo.write(f'Russas, {dia}/{mes}/{ano}.')
    linha()
    print('\033[1;32mRelatorio gerado em "dados.txt"\033[m')
    linha()
