brasileirao = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
               'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
               'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print('Lista de times do brasileirão: ', brasileirao)
print('-=' * 15)
print('Os 5 primeiros colocados são:', brasileirao[0:5])
print('-=' * 15)
print('Os ultimos 4 colocados são:', brasileirao[16:])
print('-=' * 15)
print('Times em ordem alfabética', sorted(brasileirao))
print('-=' * 15)
posicao = brasileirao.index('Corinthians') + 1
print(f'O Corinthias está na {posicao}ª Posição')
