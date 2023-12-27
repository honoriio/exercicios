import random
from time import sleep
lista_final = list()
numeros = list(range(1, 61))

print('-' * 42)
print('JOGA NA MEGA SENA'.center(42))
print('-' * 42)
quantia = int(input('Quantos jogos deseja sortear: '))
print('-' * 42)

for c in range(quantia):
    sorteios = random.sample(numeros, 6)
    sorteios.sort()  # Ordenar os números antes de adicioná-los à lista
    lista_final.append(sorteios)

print(f'SORTEANDO {quantia} JOGOS'.center(42))
print('-' * 42)
for i, l in enumerate(lista_final):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=' * 42)
print('BOA SORTE'.center(42))
print('=' * 42)