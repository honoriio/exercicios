import random

print('-' * 30)
print('          JOKENPÔ')
print('-' * 30)

escolha = ['PEDRA', 'PAPEL', 'TESOURA']
aleatorio = random.choice(escolha)

print('Escolha uma das opções: ')
print('1. PEDRA')
print('2. PAPEL')
print('3. TESOURA')

jogador = input('Digite o número da escolha: ')

if jogador == '1':
    jogador = 'PEDRA'
elif jogador == '2':
    jogador = 'PAPEL'
elif jogador == '3':
    jogador = 'TESOURA'
else:
    print('Escolha inválida. Por favor, escolha um número de 1 a 3.')
    exit()  # Terminate the game if the choice is invalid.

print('Você escolheu {}'.format(jogador))
print('A I.A escolheu {}'.format(aleatorio))

if jogador == aleatorio:
    print('EMPATE!')
elif (
    (jogador == 'PEDRA' and aleatorio == 'TESOURA') or
    (jogador == 'PAPEL' and aleatorio == 'PEDRA') or
    (jogador == 'TESOURA' and aleatorio == 'PAPEL')
):
    print('VOCÊ GANHOU!')
else:
    print('A I.A GANHOU!')

