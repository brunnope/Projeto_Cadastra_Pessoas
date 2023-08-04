from modulo import menu
import funcs_arquivo

arq = 'cadastra_pessoas.txt'

if funcs_arquivo.arqExiste(arq)== False:
    funcs_arquivo.criaArq(arq)
    

menu(arq)