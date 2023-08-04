def leiaInt():
    while True:
        try:
            inteiro = int(input('Digite sua idade: '))
        
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            inteiro = 0
            break

        except:
            print('ERRO: por favor, digite um número inteiro válido.')
        
        else:
            break
    return inteiro

def Nome():
    try:
        nome = input('Digite seu nome: ').title().strip()
    
    except:
        print('Houve um erro!')

    else:
        if nome == '':
            return 'Desconhecido'

        else:
            return nome
        
def Resp():
    resp = input('"S" para continuar ou "ENTER" para sair: ').lower().strip()

    while resp != 's' and resp != '':
        resp = input('ERRO! "S" para continuar ou "ENTER" para sair: ').lower().strip()

    return resp


#funções do arquivo:     
def arqExiste(arq):
    try:
        a = open(arq,'rt')
        a.close()
    
    except FileNotFoundError:
        return False
    
    else:
        return True

def criaArq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    
    except:
        print('Houve um Erro!')

def lerArq(arq):
    try:
        a = open(arq, 'rt')
    
    except:
        print('Erro ao tentar ler!')
    
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

def escreveArq(arq, nome, idade):
    try:
        a = open(arq,'at')
    
    except:
        print('Houve um erro!')
    
    else:
        a.write(f'{nome};{idade}\n')
        print(f'{nome} cadastrado com sucesso!')
        a.close()