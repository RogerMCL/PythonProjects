# EXERCÍCIO 106:

from time import sleep
c = ('\033[m',      # 0 - sem cor
     '\033[30;41m', # 1 - vermelho
     '\033[30;42m', # 2 - verde
     '\033[30;43m', # 3 - amarelo
     '\033[30;44m', # 4 - azul
     '\033[30;45m', # 5 - roxo
     )


def ajuda(msg):
    título(f'ACESSANDO O MANUAL DO COMANDO: \'{msg}\'', 4) # colocar string dentro de string
    print(c[5], end='')
    help(msg)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


#Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYTHON', 2)
    comando = str(input('Função ou Biblioteca >>> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('PROGRAMA CONCLUÍDO', 1)