def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
                print('\033[41mERRO!!! Por favor, digite um número inteiro válido: \033[m')
                continue
        except KeyboardInterrupt:
            print('\n\033[40mERRO!!! Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n



def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[35mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[1;33m{[c]}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mSua opção: \033[m')
    return opc

