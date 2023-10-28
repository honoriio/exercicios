print('-' * 30)
valor1 = float(input('Informe um valor inteiro :'))
print('-' * 30)
valor2 = float(input('Informe outro valor intiero :'))
print('-' * 52)

if valor1 > valor2:
    print('O valor {} é maior.'.format(valor1))
elif valor2 > valor1:
    print('O valor {} é maior.'.format(valor2))
elif valor1 == valor2:
    print('Não existe valor maior, os dois números são iguais.')
