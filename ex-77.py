valores = list()

while True:
    valor = int(input('Digite um valor: '))

    if valor in valores:
        print('Valor duplicado, não irei adicionar!')
    else:
        valores.append(valor)
        print('Valor adicinado com sucesso...')

    decisao = input('Deseja continuar [S/N]: ').upper()
    if decisao == 'N':
        break

valores.sort()
print(f'Os valores inseridos foram {valores}')
