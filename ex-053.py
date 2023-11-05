maior_idade = 21
idades = []

for i in range(0, 7):
    idade = int(input('Informe a {}° idade: '.format(i + 1)))
    idades.append(idade)
maiores = 0

for idade in idades:
    if idade >= maior_idade:
        maiores += 1

menores = 0

for idade in idades:
    if idade < maior_idade:
        menores += 1

print('''
Das idades informadas, {} pessoas são maiores de 21 anos.
Das idades informadas, {} pessoas são menores de 21 anos.
'''.format(maiores, menores))
