"""Bancário.
Escreva um programa que registre o caixa de um banco.
O programa começa perguntando se o usuário quer criar
uma conta ou fechar o programa.
Se escolher fechar o programa escreve uma mensagem de
agradecimento e fecha, caso contrário ele vai pedir que
o usuário selecione um número com 6 digitos e então se
o número não existir no registro do banco, ele irá
pedir um valor de depósito.
Depois o banco pergurará se deseja-se ver o saldo do banco,
se seim ele deverá imprimir o balanço geral do banco,
senão ele entrará em ''loop''.

"""

contas = []
depositos = []
saldo = 0


def main():
    cabeçalho('\033[33mBanco Mário de Desenvolvimento\033[m')
    print('Deseja criar conta?')
    opção = bool(int(input('1 - para ver ou criar a conta e 0 para fechar o programa: ')))
    while opção:
        criarConta()
        verSaldo()
        opção = bool(int(input('1 - para ver ou criar a conta e 0 para fechar o programa: ')))


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número válido! \033[m')
            continue
        except KeyboardInterrupt:
            print(
                '\n\033[31mERRO! Entrada de dados interrompida pelo usuário. \033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def criarConta():
    global contas, depositos, saldo
    num_conta = int(input('Digite um número de conta: '))
    while num_conta in contas:
        print('Conta já existe. Digite novamente!')
        num_conta = int(input('Digite um número de conta: '))
    contas.append(num_conta)
    deposito = float(input('Digite um valor do 1º deposito: '))
    while deposito <= 0:
        print('Valor de depósito inválido!')
        deposito = float(input('Digite o valor novamente: '))
    depositos.append(deposito)
    saldo += deposito


def verSaldo():
    global saldo
    cabeçalho('\033[35mAQUI O SEU DINHEIRO RENDE!\033[m')
    opção = bool(int(input('Deseja ver o saldo do banco? \n1 - Sim\n2 - Não\nopção>>>  ')))
    if opção:
        cabeçalho(f'\033[1;32mO seu saldo é R${saldo:.2f}\033[m')


main()
