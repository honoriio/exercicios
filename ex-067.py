print('=' * 42)
print('{:^42}'.format('HÓRUS BANK'))
print('=' * 42)

valor = int(input('Qual valor deseja sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'O total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 42)
print('Volte sempre ao Hórus Bank, tenha um bom dia!')