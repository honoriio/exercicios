import random
contador = 0
usuario = 3
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)

# Aqui criamos  a entrada da escolha para o usuario usando while.
while True:
    # aqui temos a criação da lista e dos resultados aleatorios para o jogo.
    lista = list(range(1, 1001))
    aleatorio = random.choice(lista)

    par = 3
    impar = 3

    print('--' * 20)
    print('''
    ESCOLHA UMA DAS OPÇÕES:
    [1] PAR
    [2] ÍMPAR
    ''')
    print('--' * 20)
    escolha = int(input(' : '))
    print('--' * 20)

    if escolha == 1:
        usuario = 0

    elif escolha == 2:
        usuario = 1

    # Verificando se o número e par.

    if aleatorio % 2 == 0:
        par = 0
    elif aleatorio % 2 == 1:
        impar = 1

    if usuario == par:
        contador += 1
        print('VOCÊ VENCEU!')
        print(f'O Número sorteado: {aleatorio} é PAR')
        print(f'Você Venceu {contador} vezes.')
        print('VAMOS MAIS UMA.')
    else:
        print('VOCÊ PERDEU!')
        print(f'O Número sorteado: {aleatorio} é ÍMPAR.')
        print('Fim de jogo!')
        break
