ano = int(input('Informe o ano que deseja saber se é bisexto : '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0 ):
    print('O ano de {} é bisexto '.format(ano))
else:
    print('O ano de {} não é bisexto '.format(ano))
