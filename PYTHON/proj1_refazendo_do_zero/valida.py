from defs import *
from datetime import date, datetime

def nome():
    while True:
        nome = input('Nome: ')
        if nome == '':
            print('Erro! Entrada inválida! Favor digitar seu nome corretamente!')
            continue
        if not nome.replace(' ', '').isalpha():
            print('\033[31mERRO! digite um nome válido, apenas com letras.\033[m')
        else:
            return nome.strip()
        
        
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
        if mes in [4, 6, 9, 11] and dia > 30:
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
        dia = input('Digite o dia de nascimento: ')
        mes = input('Digite o mês de nascimento: ')
        ano = input('Digite o ano de nascimento: ')

        if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
            print('\033[31mErro! Digite apenas números para o dia, mês e ano de nascimento.\033[m')
            continue

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        # Verificar se a data de nascimento é válida
        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m')
            continue

        # Verificar se o mês tem 30 ou 31 dias
        if (mes in [4, 6, 9, 11]) and dia > 30:
            print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m')
            continue

        # Verificar se fevereiro tem 28 ou 29 dias em anos bissextos
        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                if dia > 29:
                    print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m')
                    continue
            else:
                if dia > 28:
                    print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m')
                    continue

        # Se chegou até aqui, a data de nascimento é válida
        return [dia, mes, ano]


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
                 'Bairro': input('Bairro: '),
                 'Cidade': input('Cidade: '),
                 'Estado': input('Estado: '),
                 'Referência': input('Digite um ponto de referência de sua casa: ')
        }
        
        cep = input('CEP: ')
        if len(cep) != 8 or not cep.isdigit():
            print('\033[31mERRO! O CEP deve conter exatamente 8 dígitos.\033[m')
            continue
        
        dados['CEP'] = cep
        break
    
    return dados