import random

aleatorio = tuple(random.randint(1, 10) for i in range(5))
print(f'Os valores sorteados foram: {" ".join(map(str, aleatorio))}')

maior = max(aleatorio)
menor = min(aleatorio)

print(f'O maior número sorteado foi: {maior}')
print(f'O menor número sorteado foi: {menor}')
