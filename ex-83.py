numeros = list()
par = list()
impar = list()
for c in range(1, 8):
    num = int(input(f'Informe o {c}° Número: '))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

impar.sort()
par.sort()

print(f'Lista completa: {numeros}')
print(f'Números pares digitados: {par}')
print(f'Números impares digitados: {impar}')
