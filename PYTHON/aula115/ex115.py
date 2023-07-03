"""Crie um pequeno sistema modularizaqdo que permita cadastrar
pessoas pelo seu nome e idade em um arquivo de texto simples.

O sistema só vai vai ter 2 opções: CADASTRAR uma nova pessoa
e LISTAR todaas as pessoas cadastradas."""

from time import sleep
from lib.arquivo import *
from lib.interface import *

arq = 'arquivoCursoemVideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    x = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if x == 1:
        #  Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif x == 2:
        # opção para cadastrar a pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        cadastrar(arq, nome, idade)
    elif x == 3:
        cabeçalho('\033[7;34mSAINDO DO SISTEMA...\033[m')
        sleep(1)
        cabeçalho('    \033[1;41mATÉ LOGO!!!\033[m')
        break
    else:
        print('\033[31mERRO!!! Digite uma opção válida!\033[m')
        sleep(2)


