
def notas():
    # Criando a lista 
    nota = list()
    
    # Tela de apresentacao
    print('=' * 52)
    print('RECEBENDO NOTAS'.center(52))
    print('=' * 52)

    # Loop para entrada de dados pelo usuario.
    while True:
        print('-' * 52)
        valores = int(input('Informe a Nota: '))
        nota.append(valores)

        # Verificando se o usuario deseja inserir mais notas. 
        decisao = input('Deseja continuar? [S/N]: ').upper()
        if decisao == 'N':
            break
    
    # Verificando quantas notas foram inseridas. 
    quantia = len(nota)

    # Verificando qual foi a maior nota
    maior = max(nota)

    # Verificando qual foi a menor nota inserida 
    menor = min(nota)

    # Fazendo a media da turma 
    media = sum(nota) / quantia

    # Retornando as variaveis para serem usadas foram da funcao
    return quantia, maior, menor, media


# Chamando a funcao
quantia, maior, menor, media = notas()

# Tela de apresentacao de notas 
print('=' * 52)
print('MEDIA DE NOTAS'.center(52))
print('=' * 52)

print(f'foram informadas {quantia} Notas.')
print(f'A maior nota foi: {maior}')
print(f'A menor nota foi: {menor}')
print(f'A media da turma foi: {media}')
print('=' * 52)
