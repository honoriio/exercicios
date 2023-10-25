numero = int(input('Digite um numero de 0 a 9999 : '))

if 0 <= numero <= 9999:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10

    print('Numero Solicitado : {}'.format(numero))
    print('Unidade : {}'.format(unidade))
    print('Dezena : {}'.format(dezena))
    print('Centena : {}'.format(centena))
    print('Milhar : {}'.format(milhar))
else:
    print('Número fora do intervalo permitido.')
