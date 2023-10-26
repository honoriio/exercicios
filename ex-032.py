n1 = float(input('Insira o primeiro número : '))
n2 = float(input('Insira o segundo  número : '))
n3 = float(input('Insira o terceiro número : '))

maior = n1
menor = n2

if maior < n2:
    maior = n2
elif n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3
print('*' * 35)
print('O Maior número inserido foi : {}'.format(maior))
print('O Menor número inserido foi : {}'.format(menor))
