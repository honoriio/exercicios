
def leiaInt(mensagem='Digite um numero: '):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return int(entrada)
        else:
            print('\033[31mPor favor, digite um número inteiro válido.\033[0m')




# Programa principal

n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
