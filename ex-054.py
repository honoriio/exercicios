pesos = []

for i in range(5):
    peso = float(input('Informe o peso da {}° pessoa : '.format(i + 1)))
    pesos.append(peso)

# o comando len foi utilizado para verificar se algum peso foi inserido.

if len(pesos) > 0:
    mais_pesado = max(pesos)
    menos_pesado = min(pesos)
    print('-' * 45)
    print('O mais  pesado tem o peso de {} kg.'.format(mais_pesado))
    print('O menos pesado tem o pesode {} Kg.'.format(menos_pesado))
else:
    print('Nenhum peso foi inserido.')
