numeros = list()
for c in range(1, 6):
    numeros.append(int(input('Digite um valor: ')))
print('-' * 62)
print(f'Você digitou os seguintes valores {numeros}')

maior_numero = max(numeros)
posicoes_maior = [i + 1 for i, num in enumerate(numeros) if num == maior_numero]

print(f'O maior número digitado foi {maior_numero} e está nas posições : {posicoes_maior}')

menor_numero = min(numeros)
posicoes_menor = [i + 1 for i, num in enumerate(numeros) if num == menor_numero]

print(f'O menor número inserido foi {menor_numero} e está nas posições: {posicoes_menor}')
