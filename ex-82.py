pessoas = list()
peso_min = list()
peso_max = list()
cont = 0

while True:
    print('=' * 62)
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    cont += 1
    pessoa = [nome, peso]
    pessoas.append(pessoa[:])

    print('=' * 62)
    decisao = input('Deseja continuar? [S/N]: ').upper()

    if decisao == 'N':
        break

for pessoa in pessoas:
    if pessoa[1] <= 80:
        peso_min.append(pessoa)
    elif pessoa[1] >= 95:
        peso_max.append(pessoa)
print('=' * 62)
print(f'Pessoas com peso menor ou igual a 80: {peso_min}')
print(f'Pessoas com peso maior ou igual a 95: {peso_max}')
print(f'Total de pessoas cadastradas: {cont}')
print('=' * 62)
