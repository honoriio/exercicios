numero = int(input('Informe um numero inteiro : '))

binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]

print('*' * 53)
print('Escolha qual sera a base para a conversão do numero.')
print('*' * 53)
print('[1] - BINARIO')
print('[2] - OCTAL')
print('[3] - HEXADECIMAL')
print('*' * 53)
escolha = int(input(': '))
if escolha == 1:
    print('*' * 53)
    print('O valor BINÁRIO equivalente ao número {} é \033[1;32m{}\033[m'.format(numero, binario))
    print('*' * 53)
elif escolha == 2:
    print('*' * 53)
    print('O valor OCTAL equivalente ao número {} é \033[1;32m{}\033[m'.format(numero, octal))
    print('*' * 53)
elif escolha == 3:
    print('*' * 53)
    print('O valor HEXADECIMAL equivalente ao número {} é \033[1;32m{}\033[m'.format(numero, hexadecimal))
    print('*' * 53)
