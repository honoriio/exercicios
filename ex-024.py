nome = str(input('Digite um nome : '))
validacao = "silva"

if validacao in nome:
    print('O nome {} Contém silva.'.format(nome))
else:
    print('O nome {} não contém silva.'.format(nome))
