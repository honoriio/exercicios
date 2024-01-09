def area(largura, comprimento):
    total = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} e de {total} m ')



print('=' * 52)
print('CONTROLE DE TERRENOS'.center(52))
print('=' * 52)

largura = float(input('LARGURA (M): '))
comprimento = float(input('COMPRIMENTO (M): '))
print('-' * 52)
area(largura, comprimento)
print('-' * 52)