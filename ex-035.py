print('*' * 60)
valor_solicitado = float(input('Informe o valor que deseja para financiar o movel : R$'))
print('*' * 60)
salario = float(input('Informe sua renda mensal: R$'))
print('*' * 60)
anos = int(input('Informe em quantos anos deseja pagar :'))
print('*' * 60)

ano = 12
meses = (ano * anos)
parcelas = (valor_solicitado / meses)
porcento_salario = (salario * 0.30)
print('\033[1;32;40mCONFERENCIA E APROVAÇÃO\033[m')
print('\033[1;37;40m--' * 30)
print('Valor solicitado: R${:.2f}'.format(valor_solicitado))
print('--' * 30)
print('Renda mensal do solicitante: R${:.2f}'.format(salario))
print('--' * 30)
print('Tempo estimado de pagamento: {} Anos'.format(anos))
print('--' * 30)
print('Quantia de meses a pagar: {} meses'.format(meses))
print('--' * 30)
print('Valor das parcelas a pagar: R${:.2f}'.format(parcelas))
print('--' * 30)

if parcelas > porcento_salario:
    print('\033[1;30;41mNão foi possivel liberar o financimento pois, o valor da parcela excede os 30% da sua renda.\033[m')
else:
    print(
        '\033[1;30;42mParabens seu financimento foi liberado!\033[m')
