import random

numeros = [0, 1, 2, 3, 4, 5]
pense = random.choice(numeros)
print('Pensei em um numero, tente adivinhar qual é.')
numero = int(input('Insira um numero de 0 a 5 : '))
if pense == numero:
    print('Você acertou, o numero que pensei é {}'.format(pense))
else:
    print('Você errou, o número que eu pensei foi {}'.format(pense))
