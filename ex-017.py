import math

grau = float(input('Informe um Grau : '))
radianos = math.radians(grau)

print('O Seno do Ângulo {} é {:.4f}'.format(grau, math.sin(radianos)))
print('O Cosseno do Ângulo {} é {:.4f}'.format(grau, math.cos(radianos)))
print('A tangent do Ângulo {} é {:.4f}'.format(grau, math.tan(radianos)))
