def aumentar(n, a):
    ac = n * a
    n = n + ac
    return n









def diminuir(n, a):
    ac = n * a
    n = n - ac
    return n








def dobro(n):
    n = n * 2
    return n







def metade(n):
    return n / 2


def form(n):
    return f'R${n:,.2f}'


def resumo(n, a, b):
    print('-' * 52)
    print('RESUMO DO VALOR'.center(52))
    print('-' * 52)
    print(f'Preco analisado:      R${form(n)}')
    print(f'Dobro do Preco:       R${form(dobro(n))}')
    print(f'Metade do Preco:      R${form(metade(n))}')
    print(f'{a}% De aumento:      R${form(aumentar(n, a))}')
    print(f'{b}% De reducao:      R${form(diminuir(n, b))}')
    print('-' * 52)
