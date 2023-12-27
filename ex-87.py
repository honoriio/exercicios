ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    decisao = str(input('DESEJA CONTINUAR? [S/N]: ')).upper()

    if decisao == 'N':
        break

print('=' * 42)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 42)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 42)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc] [0]} São {ficha[opc] [1]}')

print('<<<< VOLTE SEMPRE >>>>')
