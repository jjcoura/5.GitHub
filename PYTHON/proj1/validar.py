import defs

def nome():
    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Erro! Entrada inválida!')
            continue
        temp = ''.join(name.split(''))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return nome.strip('')
        
        
def senha():
    while True:
        senha = input('Digite sua senha de 6 dígitos: ')
        if senha == '':
            print('Erro! Por favor digite sua senha!')
            senha = len(senha)
        if senha > 6:
            print('Senha inválida!')
            continue
        return senha.strip('')
 
 
def email():
    while True:
        email = input('Email: ')
        if email == '':
            print('Erro! Entrada inválida!')
        elif '@' and '.com' in email:
            return email.strip()
        else:
            print('Email inválido por favor corrija!')
            
            
def data():
    while True:
        data =  input('Nascimento (dd/mm/aaaa): ')
        if data == '':
            print('Erro! Entrada inválida!')
            continue
        temp = ''.join(data.split('')) 
        if not temp.isnumeric():
            print('Digite uma data válida!')
            continue
        if data.count('/') == 2 and data != '//':
            dia, mes , ano = data.split('/') 
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <=2023:
                return data.strip('')
            else:
                print('Data inválida!: por favor revise a data digitada!')
        else:
            print('A data deve seguir o padrão (dd/mm/aaaa)')
            
            
def login():
    while True:       
        login = int(input('Login: '))
        if login == '':            
             print('Erro! Login inválido!')
             continue
        return login.strip('')
    
    
def cel():
    while True:
        telefone = int(input('Digite seu telefone: '))  
        if telefone == '':
            print('Erro! Digite um número válido!')
            continue
        elif not telefone.isnumeric():
            print('Insira apenas números.')
            continue 
        else:
            if 9 <= len(telefone) <= 11:
                return telefone
            else:
                print('O número deve ter entre 9 e 11 digitos')     
                
                
def ed():
    while True:
        print('=========\033[1;32mSeu endereço completo!\033[m ========')  
        dados = {'Rua': input('Rua: '),
                 'Numero': int(input('Número: ')),
                 'Complemento': input('Complemento: '),
                 'Bairro': str(input('Bairro: ')),
                 'CEP': int(input('CEP: ')),
                 'Cidade': str(input('Cidade: ')),
                 'Referência': input('Referencia: ')}
        return dados
    
    

             