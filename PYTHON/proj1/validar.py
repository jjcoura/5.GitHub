from defs import *
from datetime import date, datetime

def nome():
    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Erro! Entrada inválida!')
            continue
        if not nome.replace(' ', '').isalpha():
            print('\033[31mERRO! digite um nome válido, apenas com letras.\033[m')
        else:
            return nome.strip('')
        
        
def senha():
    while True:
        senha = input('Digite sua senha de 6 dígitos: ')
        if senha == '':
            print('Erro! Por favor digite sua senha!')
        elif len(senha) != 6:
            print('\033[31mErro! A senha deve conter exatamente seis dígitos!\033[m')
        else:
            break
 
 
def email():
    while True:
        email = input('Email: ')
        if email == '':
            print('\033[31mErro! Entrada inválida!\033[m')
        elif '@' and '.com' in email:
            return email.strip()
        else:
            print('\033[31mEmail inválido por favor corrija!\033[m')


def validar_data(datas):
    try:
        formato = "%d/%m/%Y"
        data_formatada = datetime.strptime(data, formato)
        dia = data_formatada.day
        mes = data_formatada.month
        ano = data_formatada.year
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
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
            
            
def datas():
    while True:
        dia = input('Dia do nascimento: ')
        mes = input('Mes do nascimento: ')
        ano = input('Ano do nascimento: ')

        if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
            print('\033[31mErro! Digite apenas números para o dia, mês e ano de nascimento.\033[m' )
            continue

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m' )
            continue

        if (mes in [4, 6, 9, 11]) and dia > 30:
            print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m' )
            continue

        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                if dia > 29:
                    print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m' )
                    continue
            else:
                if dia > 28:
                    print('\033[31mData de nascimento inválida. Por favor, insira uma data válida.\033[m' )
                    continue
        return [dia, mes, ano]

            
def login():
    while True:
        print('Seu login deve conter no máximo 12 caracteres com letras maiúsculas, minúsculas, símbolos e números.' )
        login = input('Login: ')
        if login == '':            
             print('\033[31mErro! Login inválido!\033[m')
        elif len(login) > 12:
            print('\033[31mERRO! O login deve ter no máximo 12 caracteres entre letras, números e símbolos, incluindo letras maiúsculas.\033[m' )
        elif not any(char.isupper() for char in login):
            print('\033[31mERRO! O login deve conter pelo menos uma letra maiúscula.\033[m')
        elif not any(char.islower() for char in login):
            print('\033[31mERRO! O login deve conter pelo menos uma letra minúscula.\033[m' )
        elif not any(char.isdigit() for char in login):
            print('\033[31mERRO! O login deve conter pelo menos um número.\033[m' )
        elif not any(not char.isalnum() for char in login):
            print('\033[31mERRO! O login deve conter pelo menos um símbolo.\033[m' )
        else:
            return login.strip('')
    
    
def cel():
    while True:
        telefone = input('Digite seu telefone: ')
        if telefone == '':
            print('\033[31mErro! Digite um número válido!\033[m')
        elif not telefone.isnumeric():
            print('\033[31mInsira apenas números.\033[m')
        elif len(telefone) < 9 or len(telefone) > 11:
            print('\033[31mO número deve ter entre 9 e 11 digitos\033[m')
        else:
            return telefone
                
                
def ed():
    while True:
        print('=========\033[1;32mSeu endereço completo!\033[m ========')  
        dados = {'Rua': input('Rua: '),
                 'Numero': input('Número: '),
                 'Complemento': input('Complemento: '),
                 'Bairro': input('Bairro: '),
                 'Cidade': input('Cidade: '),
                 'Referência': input('Referencia: ')}

        cep = input('CEP: ')
        if len(cep) != 8 or not cep.isdigit():
            print('\033[31mERRO! O CEP deve conter exatamente 8 dígitos.\033[m' )
            continue

        dados['CEP'] = cep
        break
    return dados
