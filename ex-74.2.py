produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 42)
print('LISTA DE PREÇOS'.center(42))
print('-' * 42)

for i in range(0, len(produtos), 2):
    nome_produto = produtos[i]
    preco_produto = produtos[i + 1]
    print(f'{nome_produto:.<30} R$ {preco_produto:.2f}')

print('-' * 42)


# feito pelo chat gpt
