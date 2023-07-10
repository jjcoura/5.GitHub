import defs
from datetime import date, datetime

def nome():
    while True:
        nome = input('Nome: ')
        if nome == '':
            print('Erro! Entrada inválida! Favor digitar seu nome corretamente!')
            continue
        temp = ''.join(nome.split(''))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return nome.strip('')
        
        
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
            break
        
    
def email():
    while True:
        print('Por favor digite seu e-mail.')
        email = input('Email: ')
        if email == ' ':
            print('\033[31mErro! Email indefinido! Favor digitar um e-mail valido!\033[m')
        elif '@' and '.com' in email:
            return email.strip()
        else:
            print('\033[31mEmail incorreto por favor corrija!\033[m')
            
            
def validar_nascimento(nascimento):
    try:
        formato = "%d/%m/%Y"
        data_formatada = datetime.strptime(nascimento, formato)
        dia = data_formatada.day
        mes = data_formatada.month
        ano = data_formatada.year

        # Verificar se o mês tem 30 ou 31 dias
        if (mes in [4, 6, 9, 11]) and dia > 30:
            return False
        # Verificar se fevereiro tem 28 ou 29 dias em anos bissextos
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                if dia > 29:
                    return False
            else:
                if dia > 28:
                    return False

        return True
    except ValueError:
        return False


def nascimento():
    while True:
        nascimento = input('Data de nascimento (dd/mm/aaaa): ')
        if nascimento == '':
            print('\033[31mErro! Entrada inválida.\033[m')
            continue
        temp = ''.join(nascimento.split())
        if not temp.isnumeric():
            print('\033[31mDigite uma data de nascimento válida no formato (dd/mm/aaaa).\033[m')
        elif nascimento.count('/') == 2 and nascimento != '//':
            print('\033[31mDigite uma data de nascimento válida no formato (dd/mm/aaaa).\033[m')
        elif not validar_nascimento(nascimento):
            print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m')
        else:
            dia, mes, ano = nascimento.split('/')
            return dia, mes, ano
        

def login():
    while True:
        print('Seu login deve conter no máximo 12 caracteres com letras maiúsculas, minúsculas, símbolos e números.')
        login = input('Digite seu login: ')
        if login == '':
            print('\033[31mERRO! Login inválido!\033[m')
        elif len(login) > 12:
            print('\033[31mERRO! O login deve ter no máximo 12 caracteres entre letras, números e símbolos, incluindo letras maiúsculas.\033[m')
        elif not any(char.isupper() for char in login):
            print('\033[31mERRO! O login deve conter pelo menos uma letra maiúscula.\033[m')
        elif not any(char.islower() for char in login):
            print('\033[31mERRO! O login deve conter pelo menos uma letra minúscula.\033[m')
        elif not any(char.isdigit() for char in login):
            print('\033[31mERRO! O login deve conter pelo menos um número.\033[m')
        elif not any(not char.isalnum() for char in login):
            print('\033[31mERRO! O login deve conter pelo menos um símbolo.\033[m')
        else:
            return login.strip()
    
    
def cel():
    while True:
        cel = input('Digite seu número de telefone: ')
        if cel == '':
            print('\033[31mERRO! Entrada inválida. Digite novamente seu número de telefone!\033[m')
        elif not cel.isnumeric():
            print('\033[31mERRO! Digite apenas números.\033[m')
        elif len(cel) < 9 or len(cel) > 11:
            print('\033[31mERRO! Número de telefone inválido!\033[m')
        else:
            return cel
        
    
def endereco():
    while True:
        print('=========\033[1;32mSeu endereço completo!\033[m ========') 
        dados = {'Rua': input('Rua: '),
                 'Número': input('Número: '),
                 'Complemento': input('Complemento: '),
                 'CEP': '',
                 'Bairro': input('Bairro: '),
                 'Cidade': input('Cidade: '),
                 'Estado': input('Estado: '),
                 'Referência': input('Digite um ponto de referência de sua casa: ')
        }
        
        while len(dados['CEP']) != 8 or not dados['CEP'].isdigit():
            print('\033[31mERRO! O CEP deve conter exatamente 8 dígitos.\033[m')
            dados['CEP'] = input('CEP: ')
        
        return dados