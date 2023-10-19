carteira = float(input(print('Insira o valor que você tem na carteira : ')))

dollar = (carteira / 3.27)

carteira_formatada = f"{carteira:,.2f}"
dollar_formatado = f"{dollar:,.2f}"
print('Você tem R${} Com esse valor e possivel comprar U${} em dollar'.format(carteira_formatada, dollar_formatado))
