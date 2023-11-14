maiores_18 = 0
homens = 0
mulheres = 0
continuar = 'S'
cont = 0

while continuar == 'S':
    while True:
        try:
            print('-' * 32)
            idade = int(input('Informe a idade: '))
            if idade >= 18:
                maiores_18 += 1
            break

        except ValueError:
            print('-' * 32)

    while True:
        sexo = input('Informe o sexo [M/F]: ').upper()
        if sexo in ('M', 'F'):
            if sexo == 'M':
                homens += 1
            if sexo == 'F' and idade >= 20:
                mulheres += 1
            break
        else:
            print('-' * 32)

    cont += 1
    print('-' * 32)
    print(f'{cont} Pessoa cadastrada!')
    print('-' * 32)

    continuar = input('Quer continuar [S/N]: ').upper()

print('-' * 32)
print(f'{maiores_18} Pessoas têm mais de 18 anos!')
print(f'{homens} Homens foram cadastrados.')
print(f'{mulheres} Mulheres têm mais de 20 anos.')
print('-' * 32)
print('PROGRAMA ENCERRADO!')
print('-' * 32)
