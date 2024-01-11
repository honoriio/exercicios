from utilidades import moedas

valor = float(input('Digite o preco: R$'))

print(f'A metade de {valor} e {moedas.metade(valor)}')
print(f'O dobro de {valor} e {moedas.dobro(valor)} ')
print(f'Aumentando 10%, temos {moedas.aumentar(valor)}')
print(f'Reduzindo 13, temos {moedas.diminuir(valor)}')
