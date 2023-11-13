while True:
    print('-' * 42)
    print('Qual tabuada gostaria de ver?')
    print('-' * 42)

    numero = int(input('Digite um número (ou -1 para sair): '))

    if numero == -1:
        break

    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')
        print('-' * 42)

print('PROGRAMA ENCERRADO, VOLTE SEMPRE!')
