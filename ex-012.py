preco_produto = float(input(print('Insira o valor do produto R$: ')))

desconto = (preco_produto * 5)/100
produto_desconto = (preco_produto - desconto)

print('O valor do produto R${:.2f} com o desconto de 5% será de R${:.2f}'.format(preco_produto, produto_desconto))
