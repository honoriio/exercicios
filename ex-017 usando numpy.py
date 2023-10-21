import numpy
grau = float(input('Informe um ângulo : '))

print('O Seno do Ângulo {} é {:.4f}'.format(grau, numpy.sin(numpy.deg2rad(grau))))
print('O Cosseno do Ângulo {} é {:.4f}'.format(grau, numpy.cos(numpy.deg2rad(grau))))
print('A Tangent do Ângulo {} é {:.4f}'.format(grau, numpy.tan(numpy.deg2rad(grau))))
