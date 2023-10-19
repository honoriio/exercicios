salario = float(input(print('Informe o valor do seu salário R$:')))

aumento = (salario * 15)/100
salario_aumento = (salario + aumento)

print('O seu salário é de R${:,.3f}'.format(salario))
print('E com o aumento de 15% vai para R${:,.3f}'.format(salario_aumento))
