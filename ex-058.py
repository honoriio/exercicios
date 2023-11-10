menu = 0
while menu != 5:
    print('-' * 42)
    n1 = float(input('Insira um Número: '))
    n2 = float(input('Insira outro Número: '))

    print('-' * 42)
    print('Escolha uma das opções a baixo.')
    print('''
     [1] SOMAR
     [2] MULTIPLICAR
     [3] MAIOR
     [4] NOVOS NÚMEROS
     [5] SAIR DO PROGRAMA       
    ''')
    print('-' * 42)
    menu = int(input('Informe a opção desejada: '))

    if menu == 1:
        soma = (n1 + n2)
        print('O valor da soma dos números {} e {} é {}'.format(n1, n2, soma))

    elif menu == 2:
        soma = (n1 * n2)
        print('A multiplicação dos numeros {} e {} é igual a {}'.format(n1, n2, soma))

    elif menu == 3:
        maior = max(n1, n2)
        print('O maior número entre {} e {} é o {}'.format(n1, n2, maior))

    elif menu == 4:
        print('-' * 42)
        n1 = float(input('Insira um número: '))
        n2 = float(input('Insira outro número: '))

    elif menu == 5:
        print('Programa encerrado!')

    else:
        print('Opção invalida, escolha uma opção valida.')
