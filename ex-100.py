def fatorial(n, show=False):
    resultado = 1 
    for i in range(1, n + 1):
        resultado *= i

    if show == False:
        print('=' * 62)
        print(f'O fatorial de {n} é: {resultado}')
        print('=' * 62)
    else:
        print('=' * 62)
        print(f'5 x 4 x 3 x 2 x 1 = {resultado}')
        print('=' * 62)

numero = 5 
resultado_fatorial = fatorial(numero, show=False)
