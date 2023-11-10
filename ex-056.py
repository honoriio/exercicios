sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual e o sexo da pessoa? [M/F]')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Favor inserir um valor valido.')
print('FIM!')
