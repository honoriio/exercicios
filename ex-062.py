numero = 0
contador = 0
soma = 0
print('-' * 42)
print('Para encerrar o programa Digite 999')
print('-' * 42)
while True:
    numero = int(input('Informe um número: '))

    if numero == 999:
        break
    soma += numero
    contador += 1

print(f'Você inseriu {contador} Números.')
print(f'O valor da soma entre os numeros foram: {soma}')
print('FIM!')
