def area(a, b):
    total = a * b
    print(f'A area de um terreno {a} x {b} e de {total} m ')



print('=' * 52)
print('CONTROLE DE TERRENOS'.center(52))
print('=' * 52)

a = float(input('LARGURA (M): '))
b = float(input('COMPRIMENTO (M): '))
print('-' * 52)
area(a, b)
print('-' * 52)