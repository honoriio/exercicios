altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é de {:.2f}. Neste caso, você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print('Seu IMC é de {:.2f}. Neste caso, você está no peso ideal.'.format(imc))
elif imc >= 25.0 and imc <= 29.9:
    print('Seu IMC é de {:.2f}. Neste caso, você está com sobrepeso.'.format(imc))
elif imc >= 30.0 and imc <= 39.9:
    print('Seu IMC é de {:.2f}. Neste caso, você está com Obesidade grau 2.'.format(imc))
elif imc >= 40.0:
    print('Seu IMC é de {:.2f}. Neste caso, você está com Obesidade grau 3.'.format(imc))
