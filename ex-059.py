import math

decisao = 'S'

while decisao == 'S':
    numero = int(input('Insira um numero: '))
    fatorial = math.factorial(numero)
    print('O fatorial de {} e igual a: {}'.format(numero, fatorial))
    print('-' * 52)
    decisao = input('Deseja continuar? [S/N]: ').upper()

print('-' * 52)
print('FIM!')
