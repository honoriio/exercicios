# Importando as bibliotecas
import time
# Criando a funcao


def ajuda():
    while True:
        time.sleep(1)
        print('=' * 100)
        print('SISTEMA DE AJUDA PyHELP'.center(100))
        print('=' * 100)

        conteudo = input('Informe a funcao ou a Biblioteca: ')

        if conteudo == 'fim':
            print('-' * 100)
            print('PROGRAMA ENCERRADO, VOLTE SEMPRE QUE PRECISAR'.center(100))
            print('-' * 100)
            break

        if conteudo == 0:
            print('Valor invalido')
        else:
            print('=' * 100)
            print(f'ACESSANDO CONTEUDO DO MANUAL {conteudo}'.center(100))
            print('=' * 100)
            print(help(conteudo))






ajuda()
