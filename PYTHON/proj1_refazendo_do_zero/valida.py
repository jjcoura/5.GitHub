from defs import *
from time import date

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
def nascimento():
    while True:
        nascimento = input('Data de nascimento (dd/mm/aaaa): ')
        if nascimento == '':
            print('\033[31mErro! Entrada inválida: \033[m')
            continue
        temp = ''.join(nascimento.split())
        if not temp.isnumeric():
            print('\033[31mDigite uma data de nascimento válida sem letras simbolos ou caracteres no formato (dd/mm/aaaa). Obrigado!\033[m')
        
def login():
def cel():
def endereço():