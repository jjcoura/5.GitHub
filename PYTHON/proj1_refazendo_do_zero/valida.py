from defs import *
def nome():
    while True:
        nome = input('Nome: ')
        if nome == '':
            print('Erro! entrada inválida! Favor digite seu nome corretamente!')
            continue
        temp = ''.join(name.split(''))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return nome.strip('')
def senha():
def email():
def data():
def login():
def cel():
def endereço():