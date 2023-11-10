import random

contador = 0

while True:
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
    pense = random.choice(numeros)

    print('Pense em um número de 0 a 10 e tente adivinhar qual é!')
    palpite = int(input('Insira um palpite de 0 a 10: '))
    print('-' * 52)

    if palpite == pense:
        print('-' * 52)
        print('Você acertou! o número que eu pensei é {}'.format(pense))
        print('Você fez: {} tentativas até acertar!'.format(contador))
        break
    else:
        print('Você errou. O número que eu pensei é {}'.format(pense))
        contador += 1

print('FIM!')
