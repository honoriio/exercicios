numeros = list()

for i in range(5):
    numero = int(input('Digite un número: '))

    indice = 0
    while indice < len(numeros) and numero > numeros[indice]:
        indice += 1

    numeros.insert(indice, numero)

print('Números em ordem crescente:', numeros)
