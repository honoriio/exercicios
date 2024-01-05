pessoas = dict()

print('-' * 42)
print('Historico Escolar'.center(42))
print('-' * 42)

pessoas['Nome'] = str(input('Informe o Nome: '))
pessoas['Media'] = float(input('Informe a media: '))

if pessoas['Media'] <= 6.9:
    pessoas['Situacao'] = 'REPROVADO'
else:
    pessoas['Situacao'] = 'APROVADO'
print('=' * 42)
for chave, valor in pessoas.items():
    print(f'{chave}: {valor}')
print('=' * 42)
