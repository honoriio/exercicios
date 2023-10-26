velocidade = float(input('Informe a velocidade do carro : '))
limite = 80
excesso = (velocidade - limite)
if velocidade > limite:
    multa = excesso * 7
    print('Você Foi multado em R${:.2f} por estar  {} KM acima do limite de 80 KM'.format(multa, excesso))
else:
    print('Velocidade limite não ultrapassada.')
