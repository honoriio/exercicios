def ficha(jogador='', gols=0):
    if jogador == '':
        jogador = '<DESCONHECIDO>'

    if gols == 0:
        gols = 0

    return jogador, gols

# Recebendo os dados pelo usuário
print('=' * 62)
jogador = input('Nome do Jogador: ')
gols_str = input('Numero de Gols: ')

# Tratando o caso em que o usuário não insere dados para gols
if gols_str.isdigit():
    gols = int(gols_str)
else:
    gols = 0

print('=' * 62)

# Chama a função com os dados inseridos pelo usuário
jogador, gols = ficha(jogador, gols)

# Print do resultado
print(f'O Jogador {jogador} fez {gols} neste campeonato.')

