import os
from datetime import datetime
from valida import *

def limpaTerminal():
    """Fução que limpa a tela do terminal

    Returns:
        os : A função limpaTerminal() é responsável por limpar a tela do terminal/console, removendo qualquer conteúdo anteriormente exibido. Essa função é utilizada para proporcionar uma melhor experiência de uso ao usuário, garantindo que a interface do programa seja limpa e organizada.

A implementação da função limpaTerminal() pode variar dependendo do sistema operacional em que o programa está sendo executado. No código que você forneceu, a função faz uso da biblioteca os para detectar o sistema operacional e executar o comando correspondente para limpar a tela.

import os

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')
    
    
A função os.name retorna o nome do sistema operacional.
No caso em que os.name é igual a 'nt', o sistema operacional é Windows, então o comando 'cls' é utilizado para limpar a tela.
Caso contrário, o sistema operacional é considerado como Unix/Linux, então o comando 'clear' é utilizado para limpar a tela.
Dessa forma, quando a função limpaTerminal() é chamada, o comando correspondente ao sistema operacional é executado, realizando a limpeza da tela.

É importante ressaltar que a função limpaTerminal() pode não funcionar corretamente em alguns ambientes de desenvolvimento integrados (IDEs) ou em certas situações específicas. Em tais casos, a limpeza da tela pode não ser realizada ou pode produzir resultados indesejados.
    """
    return os.system('cls' if os.name == 'nt' else 'clear')

def linha():
    return '-' * 32

data = datetime.now()
dia = data.day
mes = data.month
ano = data.year

def menu():
    """Menu

    Returns:
        função menu: Cria um menu personalizado chamado "LOJA LEGAL" há apenas um input para chamar as opções acima para as suas devidas funções serem realizadas.
    """
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
    """Função CADASTRO:
    
    1.  Limpar a tela do terminal:
* Chama a função limpaTerminal() para limpar a tela antes de exibir as informações do cadastro.

    2.  Exibir mensagem de cabeçalho:
* Imprime na tela uma mensagem indicando que o usuário está entrando no processo de cadastro.

    3.  Solicitar nome:
* Chama a função nome() para solicitar e validar o nome do cliente. O nome deve conter apenas letras.

    4.  Solicitar login:
* Chama a função login() para solicitar e validar o login do cliente. O login deve ter no máximo 12 caracteres e conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um símbolo.

    5.  Verificar se o login já existe:
* Abre o arquivo logins.txt em modo de leitura e percorre as linhas do arquivo.
* Verifica se o login fornecido pelo usuário já existe no arquivo.
* Se o login já existir, exibe uma mensagem de erro e encerra o cadastro.
* Caso contrário, continua para a próxima etapa.

    6.  Solicitar senha:
* Chama a função senha() para solicitar e validar a senha do cliente. A senha deve ter exatamente seis dígitos.

    7.  Solicitar e-mail:
* Chama a função email() para solicitar e validar o e-mail do cliente. O e-mail deve estar em um formato válido.

    8.  Solicitar data de nascimento:
* Chama a função nascimento() para solicitar e validar a data de nascimento do cliente. A data deve ser uma data válida.

    9.  Solicitar número de telefone:
* Chama a função cel() para solicitar e validar o número de telefone do cliente. O número de telefone deve conter apenas números e ter entre 9 e 11 dígitos.

    10. Solicitar endereço:
* Chama a função endereco() para solicitar e validar o endereço completo do cliente. O endereço inclui rua, número, complemento, bairro, cidade, estado, referência e CEP.

    11. Armazenar os dados do cliente:
* Abre o arquivo logins.txt em modo de escrita (append) para adicionar os dados do cliente ao final do arquivo.
* Escreve os dados do cliente no formato apropriado, separando cada informação por um hífen (-) e cada campo com seu respectivo valor.
* Fecha o arquivo após a escrita.

12. Exibir mensagem de sucesso:
* Exibe uma mensagem indicando que o cliente foi cadastrado com sucesso.

Após executar todas essas etapas, a função cadastro() é concluída e o programa retorna ao menu principal.
    """
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
    """Função MOSTRARDADOS:

Aqui está a descrição das etapas dentro da função `mostrarDados()`:

1. Limpar a tela do terminal:
   - Chama a função `limpaTerminal()` para limpar a tela antes de exibir os dados do cliente.

2. Exibir mensagem de cabeçalho:
   - Imprime na tela uma mensagem indicando que o usuário precisa fazer login para acessar seus dados.

3. Solicitar login e senha:
   - Solicita ao usuário que digite seu login e senha.
   - Armazena o login digitado na variável `userlogin` e a senha digitada na variável `usersenha`.

4. Verificar as informações de login e senha:
   - Abre o arquivo `logins.txt` em modo de leitura e percorre as linhas do arquivo.
   - Divide cada linha em valores separados pelo caractere hífen (-).
   - Verifica se o login e a senha fornecidos pelo usuário correspondem a algum cliente cadastrado.
   - Se o login e a senha forem encontrados, exibe os dados do cliente na tela.
   - Caso contrário, exibe uma mensagem de erro informando que o login ou a senha são inválidos.

5. Exibir os dados do cliente:
   - Se as informações de login e senha forem válidas, imprime na tela os dados do cliente.
   - Percorre os valores encontrados para o cliente e os exibe um por um, formatados corretamente.
   - No caso do campo "Endereço", os dados são tratados como um dicionário e são exibidos individualmente.

6. Exibir mensagem de erro:
   - Se as informações de login e senha forem inválidas ou não correspondem a nenhum cliente cadastrado, exibe uma mensagem de erro informando que o login ou a senha são inválidos.

Após executar essas etapas, a função `mostrarDados()` é concluída e o programa retorna ao menu principal.  
    
    """
    limpaTerminal()
    print('=== < \033[1;92m        DADOS DO CLIENTE\033[m       > ===')
    linha()
    logins = open('logins.txt', 'r')
    clientes = logins.readlines()
    logins.close()
    
    if len(clientes) == 0:
        print('\033[1;31mNão há clientes cadastrados!\033[m')
        linha()
        return
    
    print('Clientes cadastrados:')
    for i, cliente in enumerate(clientes):
        print(f'{i+1}. {cliente.strip()}')
    
    while True:
        escolha_cliente = input('Digite o número do cliente para exibir os dados (ou 0 para voltar): ')
        
        if escolha_cliente == '0':
            return
        
        if not escolha_cliente.isdigit():
            print('\033[1;31mERRO! Insira um número válido.\033[m')
            linha()
            continue
        
        indice_cliente = int(escolha_cliente) - 1
        
        if indice_cliente < 0 or indice_cliente >= len(clientes):
            print('\033[1;31mERRO! Cliente inválido.\033[m')
            linha()
            continue
        
        valores = clientes[indice_cliente].split('-')
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
        break
    
    
def senha():
    """Função SENHA

    Returns:
       A função `senha()` é responsável por solicitar e validar a senha do cliente durante o processo de cadastro. Ela garante que a senha digitada tenha exatamente seis dígitos.

Aqui está a descrição das etapas dentro da função `senha()`:

1. Exibir mensagem de orientação:
   - Imprime na tela uma mensagem orientando o usuário a digitar uma senha com seis dígitos.

2. Solicitar senha:
   - Chama a função `input()` para solicitar ao usuário que digite a senha.
   - Armazena a senha digitada na variável `senha`.

3. Validar a senha:
   - Verifica se a senha possui exatamente seis dígitos.
   - Se a senha não tiver seis dígitos, exibe uma mensagem de erro e retorna ao passo 2 para solicitar uma nova senha.
   - Caso contrário, a senha é considerada válida e a função é concluída, retornando a senha digitada.

Essa é a descrição das etapas dentro da função `senha()`. Ela garante que a senha tenha o formato esperado, exigindo que tenha exatamente seis dígitos. Caso contrário, solicita ao usuário que insira uma nova senha até que seja fornecida uma senha válida.

    """
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
    """Função clientesCadastrados:
    
    A função `clientesCadastrados()` é responsável por exibir na tela todos os clientes cadastrados no arquivo `logins.txt`. Ela percorre o arquivo, lê as linhas contendo as informações dos clientes e imprime cada linha na saída.

Resumo da função `clientesCadastrados()`:

1. Limpar a tela do terminal:
   - Chama a função `limpaTerminal()` para limpar a tela antes de exibir os clientes cadastrados.

2. Exibir mensagem de cabeçalho:
   - Imprime na tela uma mensagem indicando que a lista de clientes cadastrados será exibida.

3. Abrir o arquivo `logins.txt`:
   - Abre o arquivo `logins.txt` em modo de leitura.

4. Percorrer as linhas do arquivo:
   - Utiliza um loop para percorrer cada linha do arquivo.

5. Exibir cada linha na tela:
   - Imprime cada linha lida do arquivo, que contém as informações de um cliente cadastrado.
   - Utiliza a função `print()` para exibir a linha na saída.

6. Fechar o arquivo:
   - Fecha o arquivo `logins.txt` após a leitura.

Após executar essas etapas, a função `clientesCadastrados()` é concluída e o programa retorna ao menu principal.

Essa é a descrição das etapas dentro da função `clientesCadastrados()`. Ela percorre o arquivo `logins.txt` e exibe na tela todas as linhas contendo as informações dos clientes cadastrados.

    """
    limpaTerminal()
    print('=== < \033[1;92m        CLIENTES CADASTRADOS\033[m       > ===')
    logins = open('logins.txt', 'r')
    for l in logins.readlines():
        l = l.strip()
        print(f'\033[1;92m{l}\033[m')
    logins.close()
    linha()


def relatorio():
    """Função relarotio:
    
    Descrição do que cada item da função `relatorio()`:

1. Contagem de clientes cadastrados:
   - Inicializa a variável `cc` como zero para contar o número de clientes cadastrados.
   - Inicializa a lista `nomess` para armazenar os nomes dos clientes.

2. Leitura do arquivo `logins.txt`:
   - Abre o arquivo `logins.txt` em modo de leitura.

3. Contagem e armazenamento dos nomes dos clientes:
   - Percorre cada linha do arquivo `logins.txt` utilizando um loop `for`.
   - Divide cada linha em valores separados pelo caractere hífen (-).
   - Extrai o nome do cliente da primeira informação da linha.
   - Adiciona o nome à lista `nomess`.
   - Incrementa a variável `cc` para contar o número de clientes cadastrados.

4. Fechamento do arquivo `logins.txt`:
   - Fecha o arquivo `logins.txt` após a leitura.

5. Limpeza da tela:
   - Chama a função `limpaTerminal()` para limpar a tela antes de exibir o relatório.

6. Criação do diretório `RELATORIO_proj1`:
   - Verifica se o diretório `RELATORIO_proj1` já existe.
   - Se não existir, cria o diretório utilizando a função `os.makedirs()`.

7. Criação do arquivo `dados.txt`:
   - Define o caminho do arquivo `dados.txt` no diretório `RELATORIO_proj1` utilizando a função `os.path.join()`.
   - Abre o arquivo `dados.txt` em modo de escrita (`w+`).
   - Escreve a linha de título "Relatório de Clientes" no arquivo.
   - Escreve uma linha em branco.
   - Escreve a quantidade de clientes cadastrados no arquivo.
   - Escreve uma linha em branco.
   - Percorre a lista `nomess` e escreve cada nome de cliente no arquivo, numerando-os.
   - Escreve a linha com a data atual no formato "Brasil, dia/mês/ano".
   - Fecha o arquivo `dados.txt`.

8. Exibição de mensagem de sucesso:
   - Imprime uma linha na tela indicando que o relatório foi gerado com sucesso.

Após a conclusão dessas etapas, a função `relatorio()` é finalizada e o programa retorna ao menu principal.
    """
    cc = 0
    nomess = []
    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0].split(':')[1].strip())
        cc += 1
    logins.close()
    limpaTerminal()
    
    # Criação do diretório 'RELATORIO_proj1' se não existir
    diretorio = 'RELATORIO_proj1'
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    caminho_arquivo = os.path.join(diretorio, 'dados.txt')
    arquivo = open(caminho_arquivo, 'w+')
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
    """função verifica_arquivo_logins:
    
    A função `verifica_arquivo_logins()` é responsável por verificar se o arquivo `logins.txt` existe no diretório atual. Caso o arquivo não exista, a função cria um novo arquivo vazio.

Aqui está a descrição das etapas dentro da função `verifica_arquivo_logins()`:

1. Verificar a existência do arquivo `logins.txt`:
   - Utiliza a função `os.path.exists()` para verificar se o arquivo `logins.txt` existe no diretório atual.

2. Criação do arquivo `logins.txt`:
   - Caso o arquivo `logins.txt` não exista, é aberto o arquivo em modo de escrita (`'w'`).
   - Como o arquivo ainda não existe, ele é criado vazio.

3. Fechamento do arquivo:
   - Fecha o arquivo `logins.txt` após a verificação ou criação.

Após executar essas etapas, a função `verifica_arquivo_logins()` é concluída.

Essa é a descrição das etapas dentro da função `verifica_arquivo_logins()`. Ela garante a existência do arquivo `logins.txt` no diretório atual, criando-o caso não exista. Isso é útil para garantir que o programa tenha o arquivo necessário para armazenar os dados dos clientes.

    """
    if not os.path.exists('logins.txt'):
        with open('logins.txt', 'w') as arquivo:
            arquivo.write('')

