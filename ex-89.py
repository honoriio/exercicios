import random
jogadores = dict()
dado = list([1, 2, 3, 4, 5, 6])
print('=' * 52)
print('JOGO DE DADOS'.center(52))
print('=' * 52)


for i in range(4):
    sorteio = random.choice(dado)
    jogadores['Jogador N: 1'] = sorteio
    sorteio = random.choice(dado)
    jogadores['Jogador N: 2'] = sorteio
    sorteio = random.choice(dado)
    jogadores['Jogador N: 3'] = sorteio
    sorteio = random.choice(dado)
    jogadores['Jogador N: 4'] = sorteio

for j, r in jogadores.items():
    print(f'{j}  PLACAR:  {r}')

print('=' * 52)
print('VENCEDOR'.center(52))
print('=' * 52)
print(jogadores)

print('=' * 52)
print('FIM DO JOGO!'.center(52))
