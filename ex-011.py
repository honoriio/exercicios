altura = float(input(print('Insita a altura da parede : ')))
largura = float(input(print('Insira a largura da parede : ')))

area = (altura * largura)
galoes = (area / 2)

print('A area da sua parede e de {} Metros quadrados'.format(area))
print('Será necessário {} galões de tinta para pintá la.'.format(galoes))
