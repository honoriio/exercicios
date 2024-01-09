import random
import time


numeros = []
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quantia = 5

print('=' * 62)
print('SORTEANDO E SOMANDO NUMEROS'.center(62))
print('=' * 62)

def sorteio():
    nume = random.sample(num, quantia)
    print('Sorteando 5 numeros da lista:', end=' ')
    numeros.extend(nume)

    for n in nume:
        print(n, end=' ', flush=True)
        time.sleep(0.4)
    print('PRONTO!')


def soma():
    soma_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma_pares += numero
    print(f'Somando os numeros pares de {numeros} Temos {soma_pares}')
   
    


sorteio()
soma()
print('=' * 62)
