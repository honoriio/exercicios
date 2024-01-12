from utilidades.moedas import moedas

valor = float(input('Digite o preco: R$'))

print(f'A metade de {moedas.form(valor)} e {moedas.form(moedas.metade(valor))}')
print(f'O dobro de {moedas.form(valor)} e {moedas.form(moedas.dobro(valor))} ')
print(f'Aumentando 10%, temos {moedas.form(moedas.aumentar(valor))}')
print(f'Reduzindo 13, temos {moedas.form(moedas.diminuir(valor))}')
