km = float(input('Informe a distancia da viagem em KM : '))
km_200 = 0.50
km_mais_200 = 0.45
if km <= 200:
    preco = (km * km_200)
    print('Para uma viagem de {} KM de distancia o valor e de R${:.2f}'.format(km, preco))
else:
    preco_mais_200 = (km * km_mais_200)
    print('Para uma viagem de {} KM de distancia o valor e de R${:.2f}'.format(km, preco_mais_200))
