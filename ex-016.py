import math
co = float(input('Qual o cumprimento do cateto oposto : '))
ca = float(input('Qual o comprimento do cateto adjacente : '))
hi = math.hypot(ca, co)
print('O comprimento da Hipotenusa é {:.2f}'.format(hi))
