def escreva(txt):
    tam = len(texto) + 4
    print('-' * tam)
    print(f'{txt}'.center(tam))
    print('-' * tam)
    


print('=' * 52)
print('FORMATAR TEXTO'.center(52))
print('=' * 52)

texto = input('Digite uma frase: ')
escreva(texto)
