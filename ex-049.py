soma = 0

for i in range(6):
    numero = int(input('Informe um {}º valor inteiro : '.format(i + 1)))
    if numero % 2 == 0:
        soma += numero

print('O resultado da soma dos numeros pares são {}'.format(soma))
