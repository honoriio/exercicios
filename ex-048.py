print('-' * 35)
numero = int(input('Qual tabuada gostaria de ver? :'))
print('-' * 35)

for i in range(1, 11):
    resultado = numero * i
    print('{} x {} = {}'.format(numero, i, resultado))
print('-' * 35)
print('FIM!')
