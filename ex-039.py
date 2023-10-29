print('-' * 35)
nota_1 = float(input('Insira a primeira nota : '))
print('-' * 35)
nota_2 = float(input('Insira a segunda nota : '))

media = (nota_1 + nota_2) / 2

if media < 5:
    print('-' * 35)
    print('Sua foi {}'.format(media))
    print('\033[1;31mREPROVADO\033[m')
elif (media == 5) or (media <= 6.9):
    print('-' * 35)
    print('Sua media foi {}'.format(media))
    print('\033[1;31mRECUPERAÇÃO\033[m')
elif media > 7:
    print('-' * 35)
    print('Sua media foi {}'.format(media))
    print('\033[1;32mAPROVADO\033[m')
elif media <= 0:
    print('Valores inseridos invalidos.')
