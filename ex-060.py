numero = 0
soma = 0
contador = 0
maior = float('-inf')  # Inicializar com infinito negativo para garantir que qualquer número seja maior
menor = float('inf')  # Inicializar com infinito positivo para garantir que qualquer número seja menor

print('-' * 42)
print('PARA SAIR DIGITE 999')
print('-' * 42)

while True:
    numero = int(input('Informe um número: '))

    # Verificar se o usuário deseja sair
    if numero == 999:
        break

    soma += numero
    contador += 1

    # Atualizar menor e maior números
    menor = min(menor, numero)
    maior = max(maior, numero)

# Certificar-se de que pelo menos um número foi inserido antes de calcular a média
if contador > 0:
    media = soma / contador
    print('A soma dos valores inseridos foram: {}'.format(soma))
    print('A média dos números inseridos é: {:.2f}'.format(media))
    print('O menor número inserido foi: {}'.format(menor))
    print('O maior número inserido foi: {}'.format(maior))
else:
    print('Nenhum número foi inserido.')

print('FIM!')
