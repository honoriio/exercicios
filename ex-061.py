soma = 0
contador = 0
media = 0
maior = float('-inf')
menor = float('inf')
numero = 0
decisao = 'S'  # Inicialize a variável decisao

while decisao == 'S':
    numero = int(input('Insira um número: '))
    soma += numero
    contador += 1
    decisao = input('Deseja continuar? [S/N]: ').upper()

    # Atualizar menor e maior números
    menor = min(menor, numero)
    maior = max(maior, numero)

if contador > 0:
    media = soma / contador
    print('-' * 52)
    print('Você inseriu {} números'.format(contador))
    print('A soma dos números inseridos foi: {}'.format(soma))
    print('A média dos números inseridos foi de {:.2f}'.format(media))
    print('O maior número inserido foi o {}'.format(maior))
    print('O menor número inserido foi o {}'.format(menor))
    print('-' * 52)
else:
    print('Nenhum número foi inserido.')

print('FIM!')
print('-' * 52)
