numeros = list()

while True:
    valor = int(input('Digite um número: '))
    numeros.append(valor)
    decisao = input('Deseja continuar [S/N]: ').upper()
    if decisao == 'N':
        break

digitos = len(numeros)

validacao = numeros.count(5)
orden = sorted(numeros)
decrescente = sorted(numeros, reverse=True)
if validacao <= 0:
    print('-' * 72)
    print('O número 5 não foi digitado nenhuma vez.')
else:
    print('-' * 72)
    print(f'O número 5 foi digitado: {validacao} vezes')
print('-' * 72)
print(f'Os números inseridos foram: {orden}')
print('-' * 72)
print(f'{digitos} Números foram digitados')
print('-' * 72)
print(f'Números digitados em ordem decrescente: {decrescente}')
print('-' * 72)
