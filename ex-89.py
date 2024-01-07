import random

jogadores = dict()
dado = list([1, 2, 3, 4, 5, 6])

print('=' * 52)
print('JOGO DE DADOS'.center(52))
print('=' * 52)

# Inicializa os placares dos jogadores
for i in range(1, 5):
    jogadores[f'Jogador N: {i}'] = 0

# Realiza quatro rodadas
for _ in range(1):
    for jogador in jogadores:
        sorteio = random.choice(dado)
        jogadores[jogador] += sorteio

# Exibe os placares dos jogadores
for jogador, placar in jogadores.items():
    print(f'{jogador}  PLACAR:  {placar}')

print('=' * 52)
print('VENCEDOR'.center(52))
print('=' * 52)

# Encontra e exibe o vencedor (jogador com o maior placar)
vencedor = max(jogadores, key=jogadores.get)
print(f'O vencedor é {vencedor} com um placar de {jogadores[vencedor]} pontos.')

print('=' * 52)
print('FIM DO JOGO!'.center(52))
