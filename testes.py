valor1 = int(input('Informe um valor: '))
valor2 = int(input('Informe outro valor: '))
try:
    resultado = valor1 / valor2
    print(resultado)
except:
    print(f'{valor2} nao pode ser dividido')