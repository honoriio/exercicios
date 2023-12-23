numeros = list()
par = list()
impar = list()

while True:
    valor = int(input('Digite um Número: '))
    numeros.append(valor)

    decisao = input('Deseja continuar [S/N]: ').upper()
    if decisao == 'N':
        break

for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('=' * 62)
print(f'Os números digitados foram: {numeros}')
print('=' * 62)
print(f'Os Números pares inseridos foram {par}')
print('=' * 62)
print(f'Os Números impares inseridos foram {impar}')
print('=' * 62)
