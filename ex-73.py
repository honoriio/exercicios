valores = ()

for i in range(4):
    valor = int(input('Informe um número: '))
    valores += (valor,)
print('O número 9 apareceu ', valores.count(9), 'vezes')

try:
    posicao_3 = valores.index(3) + 1
    print(f'O número 3 ésta na posição: {posicao_3}')
except ValueError:
    print('O número 3 não foi digitado em nenhuma posição.')
pares = [x for x in valores if x % 2 == 0]
print(f'Os números pares são:', ' '.join(map(str, pares)))
