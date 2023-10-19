carteira = float(input(print('Insira o valor que você tem na carteira : ')))

dollar = (carteira / 5.06)
euro = (carteira / 5.35)
libra_esterlina = (carteira / 6.15)

carteira_formatada = f"{carteira:,.2f}"
dollar_formatado = f"{dollar:,.2f}"
euro_formatado = f"{euro:,.2f}"
libra_formatado = f"{libra_esterlina:,.2f}"
print('Você tem R${} Com esse valor e possivel comprar U${} em dollar'.format(carteira_formatada, dollar_formatado))
print('Você tem R${} Com esse valor e possivel comprar U${} em euro'.format(carteira_formatada, euro_formatado))
print('Você tem R${} Com esse valor e possivel comprar U${} em libra esterlina'.format(carteira_formatada, libra_formatado))
