print('-' * 42)
print('BARATÃO DOIDO')
print('-' * 42)
cont = 0
soma = 0
mais_de_mil = 0
nome_barato = ('', float('inf'))  # Inicializa com um valor muito alto

while True:
    print('-' * 42)
    produto = input('Informe o nome do produto: ')
    valor = float(input('Informe o valor do produto: '))
    print('-' * 42)

    cont += 1
    soma += valor

    if valor >= 1000:
        mais_de_mil += 1

    if valor < nome_barato[1]:
        nome_barato = (produto, valor)

    continuar = input('Deseja continuar? [S/N]').upper()

    if continuar == 'N':
        break

print('-' * 42)
print(f'Você adicionou {cont} itens à lista.')
print(f'O nome do item mais barato é {nome_barato[0]} com valor R${nome_barato[1]:.2f}.')
print(f'Foram adicionados {mais_de_mil} produtos mais caros que R$1000,00.')
print(f'O valor total de todos os itens foi de R${soma:.2f}')
print('-' * 42)
print('PROGRAMA ENCERRADO!')
