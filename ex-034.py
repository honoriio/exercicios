reta1 = float(input('Insira o comprimento da primeira reta : '))
reta2 = float(input('Insira o comprimento da segunda reta  : '))
reta3 = float(input('Insira o comprimento da terceira reta : '))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('É possivel formar um Triangulo com os comprimemntos fornecidos.')
else:
    print('Não e possovel formar um triangulo com os comprimentos fornecidos.')
