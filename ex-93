# Dicionario e listas 
jogadores = dict()

# Apresentação do programa
print('=' * 52)
print('CADASTRO DE JOGADORES'.center(52))
print('=' * 52)

# laco while para entrada de dados atraves do usuario 
while True:
    nome = input('Jogador: ').upper()
    partidas = int(input('Partidas Jogadas: '))

    print('-' * 52)

    # Coleta de gols por partida, usando como base as partidas jogadas
    gols = []
    for partida in range(partidas):
        gols_partida = int(input(f'Quantos Gols na partida {partida + 1}?: '))
        gols.append(gols_partida)

    print('=' * 52)

    # Criando jogador e associando cada um ao dicionario correspondente
    jogador = {'jogador': nome, 'partidas': partidas, 'gols': gols}
    jogadores[nome] = jogador

    # Verificacao se o programa deve continuar com o cadastro 
    decisao = input('Deseja continuar? [S/N]: ').upper()
    print('-' * 52)

    # Verificacao da decisao do usuario 
    if decisao == 'N':
        break

# Verificando quantos jogadores foram cadastrados
quantia_jogadores = len(jogadores)

# Verificando se deseja ver os jogadores cadastrados 
dec = input('Deseja exibir os detalhes dos jogadores? [S/N]: ').upper()

# Verificacao e exibicao de dados sobre os jogadores
if dec == 'S':
    print('=' * 52)
    print('JOGADORES CADASTRADORS'.center(52))
    print('=' * 52)
    
    cont = 0
    for cont,(nome_jogadores, jogador) in enumerate(jogadores.items()):
        print(f"Jogador: {cont + 1} Nome: {jogador['jogador']}")
    print('-' * 52)

    while True:
        escolha = int(input('Deseja ver os detalhes de qual jogador?: '))

    # Verifica se a escolha do usuário é válida
        if 1 <= escolha <= quantia_jogadores:
            nome_escolhido = list(jogadores.keys())[escolha - 1]
            jogador_escolhido = jogadores[nome_escolhido]

            # Calcula a soma total de gols do jogador escolhido
            soma_gols = sum(jogador_escolhido['gols'])

            print('=' * 52)
            print(f'DETALHES DO JOGADOR {nome_escolhido}'.center(52))
            print('=' * 52)
            print(f"Partidas Jogadas: {jogador_escolhido['partidas']}")
            print(f"Gols por Partida: {jogador_escolhido['gols']}")
            print(f"Soma Total de Gols: {soma_gols}")
            print('-' * 52)
        else:
            print('-' * 52)
            print('Não existem jogadores com o número escolhido.')
            print('-' * 52)
        
        deci = input('Deseja continuar? [S/N]: ').upper()
        print('-' * 52)

        if deci == 'N':
            break

print('-' * 52)
print('PROGRAMA FINALIZADO'.center(52))
print('VOLTE SEMPRE'.center(52))
print('_' * 52)