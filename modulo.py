from time import sleep
import funcs_arquivo

def menu(arq):
    while True:

        print('-'*40)
        print(f'{"MENU PRINCIPAL":^40}')
        print('-'*40)
        
        print(f'1 - Ver pessoas cadastradas')
        print(f'2 - Cadastrar nova pessoa')
        print(f'3 - Sair do Sistema')

        print('-'*40)

        while True:

            try:
                opc = int(input('Sua opção: '))
            
            except:
                print('ERRO! por favor, digite um número inteiro válido.')

            else:
                if opc < 1 or opc > 3:
                    print('ERRO! Digite uma opção válida!')
                break
        
        sleep(1)

        if opc == 1:
            print('-'*40)
            print(f'{"VER PESSOAS CADASTRADAS":^40}')
            print('-'*40)

            funcs_arquivo.lerArq(arq)

            print()
            input('Aperte qualquer tecla para voltar: ')

        elif opc == 2:
            print('-'*40)
            print(f'{"CADASTRAR NOVAS PESSOAS":^40}')
            print('-'*40)

            while True:

                nome = funcs_arquivo.Nome()
                idade = funcs_arquivo.leiaInt()
                
                funcs_arquivo.escreveArq(arq,nome,idade)
                print()

                resp = funcs_arquivo.Resp()

                if resp == '':
                    break
                
                print()

        elif opc == 3:
            print('-'*40)
            print(f'{"Saindo do sistema... Até logo!":^40}')
            print('-'*40)
            break
