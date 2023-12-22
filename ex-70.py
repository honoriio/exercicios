extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

escolha = int(input('Digite um número entre 0 e 20: '))
while True:
    if escolha < 0 or escolha > 20:
        escolha = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    elif escolha >= 0 or escolha <= 20:
        break
print('Você digitou o número ', extenso[escolha])
