import validar
import datetime
import os

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def linha():
    return '-' * 32

data = datetime.datetime.now()
dia = data.day
mes = data.mouth
ano = data.year

def menu():
    print('''========= <<< \033[1;96m "LOJA LEGAL" \033[m >>> =========\n
             |   \033[1;36m[1]          \033[m Cadastrar Cliente    |\n
             |   \033[1;36m[1]          \033[m Dados do Cliente     |\n
             |   \033[1;36m[1]          \033[m Mostrar Clientes     |\n
             |   \033[1;36m[1]          \033[m Gerar Relatório      |\n
             |   \033[1;36m[1]          \033[m Sair                 |\n
             ______________________________________''')
    x = input('\033[1;36mDigite uma das opções acima: \033[m')
    print('________________________________________')
    return x

# definições: Cadastrar, Checar login existente, adicionar dados no arquivo txt
def cadastro():
    limpaTerminal()
    print('=== < \033[1;92m        CADASTRAR USUÁRIO\033[m       > ===')
    nome = validar.nome()
    login = validar.login()  
lerlogins = open('logins.txt', 'rt') # conferir se já tem login cadastrado
for linha in lerlogins.readlines():
    valores = linha.split('-')
    if login == valores[1].split(':')[1].strip(): # Cria lista com valores da linha
        limpaTerminal()
        linha()
        print('\033[1;31mLOGIN EXISTENTE!\033[m')
        linha()
     
    lerlogins.close()
    
    senha    = validar.senha()
    email    = validar.email()
    data     = validar.data()
    telefone = validar.cel()
    endereço = validar.ed()
    
    limpaTerminal()
    linha()
    print('\033[1;32mCLIENTE CADASTRADO COM SUCESSO!\033[m')
    linha()
    
    logins = open('logins.txt', 'a')
    logins.write(f'Nome: {nome} - Login: {login} - Senha: {senha} - Email: {email}'
                 f'- Data de Nascimento: {data} - Número de celular: {cel} - '
                 f'Endereço: {ed}\n')    
    logins.close()
                


def mostrarDados():
    limpaTerminal()
    print('=== < \033[1;92m        DADOS DO CLIENTE\033[m       > ===')
    linha()
    print('\033[1;31mlogue para acessar os seus dados!\033[m ')
    linha()
    userlogin = input('Login: ')
    usersenha = input('Senha: ')
    
    validar = False
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        valores = linha.split('-')
        if userlogin == valores[1].split(':')[1].strip and usersenha in valores[2].strip():
            limpaTerminal()
            linha()
            print('\033[1;32mCliente Logado! Dados do usuário:\033[m')
            linha()
            for percorre in range(len(valores)):
                if valores[percorre].split(':')[0] == 'Endereço':
                    dictEndereço = eval(valores[percorre].split('Endereço: ')[1])
                    for chave in dictEndereço:
                        print(f'{chave: {dictEndereço[chave]}}')
                else:
                    print(valores[percorre])
            linha()
            validar = True
            logins.close()
            break        
    if not valida:
        limpaTerminal()
        linha()
        print('\033[1;31mERRO! logoin ou senha inválidos!\033[m')
        linha()
        
 
 
 # exibir todos os clientes já cadastrados       
def clientesCadastrados(): 
    limpaTerminal()
    print('=== < \033[1;92m        CLIENTES CADASTRADOS\033[m       > ===')   
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        l = linha.split('-')
        print(f'\033[1;92m]{l[0]} | {l[1]}\033[m') 
    linha()  
    return
        
        
def relatorio():
    countClient = 0 
    nomess = []
    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0])
        countClient += 1
        
    limpaTerminal()
    arquivo = open('dados.txt', 'w+')
    arquivo.write('Relatório de Clientes\n')
    arquivo.write(f'A loja LEGAL possui {countClient} clientes(s)\n')    
    
    for i in range(len(nomess)):
        arquivo.write(str(f'{i + 1}.{nomess[1].split(":")[1]}\n'))
    arquivo.write(f'Russas, {dia}/{mes}/{ano}.')
    linha()
    print('\033[1;32mRelatorio gerado em "dados.txt"\033[m')
    linha()
    arquivo.close()
    return
       