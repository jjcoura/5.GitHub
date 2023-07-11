from defs import *
from datetime import date, datetime

def nome():
    """função nome:    

    Returns:
        A função `nome()`:

A função `nome()` é responsável por solicitar e validar o nome do cliente durante o processo de cadastro. Ela garante que o nome fornecido contenha apenas letras, sem números ou caracteres especiais.

Aqui está a descrição das etapas dentro da função `nome()`:

1. Solicitar nome:
   - Utiliza a função `input()` para solicitar ao usuário que digite o nome.

2. Validar o nome:
   - Verifica se o nome fornecido contém apenas letras, sem números ou caracteres especiais.
   - Se o nome não estiver de acordo com o critério, exibe uma mensagem de erro e retorna ao passo 1 para solicitar um novo nome.
   - Caso contrário, o nome é considerado válido e a função é concluída, retornando o nome digitado.

Essa é a descrição das etapas dentro da função `nome()`. Ela garante que o nome fornecido seja válido, consistindo apenas de letras.

    """
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
    """função senha: 
    
    Descrevendo da função `senha()`:

A função `senha()` é responsável por solicitar e validar a senha do cliente durante o processo de cadastro. Ela garante que a senha digitada tenha exatamente seis dígitos.

Aqui está a descrição das etapas dentro da função `senha()`:

1. Exibir mensagem de orientação:
   - Imprime na tela uma mensagem orientando o usuário a digitar uma senha com seis dígitos.

2. Solicitar senha:
   - Utiliza a função `input()` para solicitar ao usuário que digite a senha.
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
            break
        
    
def email():
    """função email:

    Returns:
        Função `email()`:

A função `email()` é responsável por solicitar e validar o e-mail do cliente durante o processo de cadastro. Ela verifica se o e-mail fornecido possui um formato válido, contendo o caractere "@" e o domínio ".com".

Aqui está a descrição das etapas dentro da função `email()`:

1. Solicitar e-mail:
   - Utiliza a função `input()` para solicitar ao usuário que digite o e-mail.

2. Validar o e-mail:
   - Verifica se o e-mail contém o caractere "@" e o domínio ".com".
   - Se o e-mail não estiver no formato válido, exibe uma mensagem de erro e retorna ao passo 1 para solicitar um novo e-mail.
   - Caso contrário, o e-mail é considerado válido e a função é concluída, retornando o e-mail digitado.

Essa é a descrição das etapas dentro da função `email()`. Ela garante que o e-mail fornecido seja válido, verificando se possui o formato esperado com o caractere "@" e o domínio ".com".

    """
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
    """função validar_nascimento(nascimento):

    Args:
        nascimento (_type_list): _description_ 
        A função `nascimento()` é uma função que retorna uma lista de valores. 

A função `nascimento()` solicita ao usuário que digite o dia, mês e ano de nascimento e retorna esses valores em uma lista. A lista contém três elementos: o dia, o mês e o ano fornecidos pelo usuário.

Exemplo de uso da função `nascimento()`:

```python
data_nascimento = nascimento()
print(data_nascimento)  # Saída: [10, 5, 1990]
```

No exemplo acima, a função `nascimento()` é chamada e o usuário digita o dia 10, o mês 5 e o ano 1990. A função retorna a lista `[10, 5, 1990]`, que pode ser atribuída a uma variável para posterior uso.

Portanto, o tipo de retorno da função `nascimento()` é `list`.

    Returns:
    
        Descrevando da função `validar_nascimento(nascimento)`:

A função `validar_nascimento(nascimento)` é responsável por verificar se uma data de nascimento fornecida é válida. Ela recebe como entrada uma data no formato de string e realiza uma série de verificações para garantir que a data seja uma data válida, considerando os meses com 30 ou 31 dias e o mês de fevereiro em anos bissextos.

Aqui está a descrição das etapas dentro da função `validar_nascimento(nascimento)`:

1. Verificar o formato da data:
   - Utiliza a função `strptime()` do módulo `datetime` para converter a string de data fornecida em um objeto `datetime`.
   - Caso ocorra uma exceção do tipo `ValueError`, retorna `False` indicando que a data é inválida.

2. Validar o dia e o mês:
   - Obtém o dia, mês e ano a partir do objeto `datetime`.
   - Verifica se o mês possui 30 ou 31 dias, considerando os meses 4, 6, 9 e 11.
   - Verifica se o mês é fevereiro (valor 2) e, se for, verifica se o ano é bissexto.
   - Retorna `False` se o dia ou o mês forem inválidos.

3. Retornar o resultado:
   - Se todas as verificações passarem com sucesso, retorna `True` indicando que a data de nascimento é válida.

Essa é a descrição das etapas dentro da função `validar_nascimento(nascimento)`. Ela realiza a validação de uma data de nascimento, verificando se a data fornecida é válida de acordo com as regras de calendário.

    """
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
    """função nascimento:

    Returns:
        A função `def nascimento():` está sendo utilizada no programa para solicitar ao usuário que digite o dia, mês e ano de nascimento. Ela é responsável por validar e retornar os valores fornecidos pelo usuário em uma lista.

1. Solicitação de dados de nascimento:
   - A função `nascimento()` é chamada em determinado ponto do programa, onde se deseja obter a data de nascimento do cliente.
   - Ela exibe mensagens solicitando ao usuário que digite o dia, mês e ano de nascimento.

2. Validação dos dados de nascimento:
   - A função verifica se os valores fornecidos pelo usuário são numéricos, utilizando a função `isdigit()`.
   - Verifica se o dia, mês e ano são válidos, de acordo com as regras de calendário.
   - Se algum valor não for válido, a função exibe uma mensagem de erro e solicita que o usuário insira novamente os dados corretos.

3. Retorno dos dados de nascimento:
   - Após a validação dos valores fornecidos pelo usuário, a função retorna os dados em uma lista, onde o primeiro elemento é o dia, o segundo é o mês e o terceiro é o ano.
   - Essa lista pode ser armazenada em uma variável para ser utilizada posteriormente no programa.

O comportamento da função `def nascimento():` é de solicitar e validar os dados de nascimento do usuário, garantindo que sejam valores numéricos e obedecendo às regras de calendário. Ela retorna esses valores em uma lista para serem utilizados no restante do programa.


    """
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
    """função login:

    Returns:       

A função `login()` é responsável por solicitar e validar o login do cliente durante o processo de cadastro. Ela garante que o login atenda a determinados critérios, como ter no máximo 12 caracteres, conter letras maiúsculas, letras minúsculas, números e símbolos.


1. Exibir mensagem de orientação:
   - Imprime na tela uma mensagem orientando o usuário a digitar um login válido.

2. Solicitar login:
   - Utiliza a função `input()` para solicitar ao usuário que digite o login.
   - Armazena o login digitado na variável `login`.

3. Validar o login:
   - Verifica se o login tem no máximo 12 caracteres, utilizando a função `len()`.
   - Verifica se o login contém pelo menos uma letra maiúscula, utilizando a função `isupper()`.
   - Verifica se o login contém pelo menos uma letra minúscula, utilizando a função `islower()`.
   - Verifica se o login contém pelo menos um número, utilizando a função `isdigit()`.
   - Verifica se o login contém pelo menos um caractere não alfanumérico, utilizando a função `isalnum()`.
   - Se o login não atender a algum dos critérios acima, exibe uma mensagem de erro e retorna ao passo 2 para solicitar um novo login.
   - Caso contrário, o login é considerado válido e a função é concluída, retornando o login digitado.

Essa é a descrição das etapas dentro da função `login()`. Ela garante que o login fornecido atenda aos critérios estabelecidos, incluindo comprimento máximo, presença de letras maiúsculas, minúsculas, números e caracteres especiais. Caso o login não atenda a esses critérios, solicita ao usuário que insira um novo login até que seja fornecido um login válido.

    """
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
    """a função cel de telefone celular:

    Returns:
        

A função `cel()` é responsável por solicitar e validar o número de telefone celular do cliente durante o processo de cadastro. Ela verifica se o número fornecido contém apenas dígitos numéricos e se está dentro de um intervalo válido de comprimento.

Descrição:

1. Solicitar número de telefone:
   - Utiliza a função `input()` para solicitar ao usuário que digite o número de telefone celular.

2. Validar o número de telefone:
   - Verifica se o número fornecido contém apenas dígitos numéricos, utilizando a função `isdigit()`.
   - Verifica se o número de telefone possui um comprimento válido.
   - Se o número de telefone não atender aos critérios acima, exibe uma mensagem de erro e retorna ao passo 1 para solicitar um novo número de telefone.
   - Caso contrário, o número de telefone é considerado válido e a função é concluída, retornando o número digitado.

Essa é a descrição das etapas dentro da função `cel()`. Ela garante que o número de telefone celular fornecido seja válido, verificando se contém apenas dígitos numéricos e se possui um comprimento dentro de um intervalo válido.

    """
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
    """função endereco:

    Returns:
        Descrevendo a função `endereco()`:

A função `endereco()` é responsável por solicitar e validar o endereço completo do cliente durante o processo de cadastro. Ela solicita informações como rua, número, complemento, bairro, cidade, estado e ponto de referência, e retorna essas informações em um dicionário.

Etapas:

1. Solicitar informações do endereço:
   - Utiliza a função `input()` para solicitar ao usuário que digite as informações do endereço, como rua, número, complemento, bairro, cidade, estado e ponto de referência.

2. Armazenar informações do endereço em um dicionário:
   - Cria um dicionário vazio chamado `dados` para armazenar as informações do endereço.
   - Utiliza a função `input()` para solicitar cada informação do endereço individualmente e armazena o valor fornecido pelo usuário no dicionário `dados`, utilizando as chaves correspondentes.

3. Solicitar o CEP (opcional):
   - Utiliza a função `input()` para solicitar ao usuário que digite o CEP do endereço.
   - Verifica se o CEP possui o comprimento correto (8 dígitos) e se contém apenas dígitos numéricos.
   - Caso o CEP não atenda aos critérios acima, o valor é armazenado como uma string vazia no dicionário `dados`.

4. Retornar o dicionário com as informações do endereço:
   - Após solicitar e armazenar todas as informações do endereço, a função retorna o dicionário `dados`, que contém as informações completas do endereço.

Essa é a descrição das etapas dentro da função `endereco()`. Ela solicita e valida as informações completas do endereço do cliente, armazenando essas informações em um dicionário. O dicionário é então retornado pela função, permitindo que as informações do endereço sejam utilizadas posteriormente no programa.

    """
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
            dados['CEP'] = cep
        break
    
    return dados