# Dicionario e listas
aproveitamento = dict()
gols = list()

# Apresentação do programa
print('=' * 52)
print('APROVEITAMENTO JOGADORES'.center(52))
print('=' * 52)

# Entrada de dados pelo usuario
aproveitamento['Nome'] = input('Nome Do Jogador: ')
aproveitamento['Partidas'] = int(input('Partidas Jogadas? :'))

print('-' * 52)

# Coleta de gols por partida, usando como base as partidas jogadas
for partida in range(aproveitamento['Partidas']):
    gols_partidas = int(input(f'Quantos Gols na partida {partida + 1}?: '))
    gols.append(gols_partidas)
print('=' * 52)

# atribuir a quantia de gols por partida a lista
aproveitamento['Gols'] = gols

# Soma dos gols
soma_gols = sum(gols)

# Atribuido a soma dos gols ao dicionario
aproveitamento['Soma Gols'] = soma_gols


# Mostrando o resultado ao usuario de forma formatada
print('=' * 52)
print('RESULTADO DO APROVEITAMENTO'.center(52))
print('=' * 52)

print(f"{'Nome do Jogador:':<30} {aproveitamento['Nome']}")
print(f"{'Partidas Jogadas:':<30} {aproveitamento['Partidas']}")

print('-' * 52)
print("Gols por Partida:")
for i, gols_partida in enumerate(aproveitamento['Gols'], 1):
    print(f"Partida {i}: {gols_partida}")

print('-' * 52)
print(f"{'Soma Total de Gols:':<30} {aproveitamento['Soma Gols']}")
print('=' * 52)
