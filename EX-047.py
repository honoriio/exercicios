soma = 0
for n in range(1, 501):
    if n % 3 == 0:
        soma += n
print('A soma dos números impares multiplos de 3 entre 1 e 500 são: {}'.format(soma))
