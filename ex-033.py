salario = float(input('Informe seu salario R$'))
base = 1250
if salario >= base:
    aumento = (salario * 10) / 100
    salario_aumento = (salario + aumento)
    print('O salário no valor de R${:.2f} com o aumento de R${:.2f} equivalente a 10% foi para R${:.2f}'.format(salario, aumento, salario_aumento))
else:
    aumento_15 = (salario * 15) / 100
    salario_aumento = (salario + aumento_15)
    print('O salário no valor de R${:.2f} com o aumento de R${:.2f} equivalente a 15% foi para R${:.2f}'.format(salario, aumento_15, salario_aumento))
