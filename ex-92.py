
# Listas e dicionarios
pessoas = list()
mulheres = list()
acima_da_media = list()


# Apresentação
print('=' * 52)
print('CADASTRO DE PESSOAS'.center(52))
print('=' * 52)

 
# Loop para entrada de dados pelo usuário
while True:
    nome = str(input('Nome: '))
    
    # Verificando se os valores foram inseridos corretamente
    if not nome.isalpha():
        while True:
            nome = str(input('Valor invalido. Nome: '))
            if nome.isalpha():
                break
            
    idade = input('Idade: ')
    sexo = input('Sexo [M/F]: ').upper()
    
    # Verificando se o valor foi inserido corretamente na variável sexo 
    if sexo != "M" and sexo != "F":
        while True:
            sexo = input('Valor inválido. Digite [M/F]: ').upper() 

            # Verificando se o valor foi inserido corretamente
            if sexo == "M" or sexo == "F":
                break

    print('-' * 52)

    pessoa = {'Nome' : nome, 'Idade' : idade, 'Sexo' : sexo}
    pessoas.append(pessoa)

    # Decisão se irá continuar a entrada de dados 
    decisao = input('Deseja continuar [S/N]: ').upper()
    print('-' * 52)

    if decisao == 'N':
        break

# verificacao de quantas pessoas foram cadastradas
quantia_pessoas = len(pessoas)

# Soma das idades para fazer a media do grupo 

soma_idades = 0
for pessoa in pessoas:
    soma_idades += pessoa['Idade']

# Validacao da media da idade do grupo cadastrado 
media_idades = soma_idades / quantia_pessoas if quantia_pessoas > 0 else 0

mulheres = [pessoa for pessoa in pessoas if pessoa['Sexo'] == 'F']


# Validacao de pessoas acima da media
acima_da_media = [pessoa for pessoa in pessoas if pessoa['Idade'] >= media_idades]

# Apresentacao dos dados cadastrados   
print('=' * 52)
print('PESSOAS CADASTRADAS'.center(52))
print('=' * 52)

# laco para o print das informacoes 
for pessoa in pessoas:
    
    print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Sexo: {pessoa['Sexo']}")
    print('-' * 52)


# print mulheres cadastradas
print('=' * 52) 
print('MULHERES CADASTRADAS'.center(52))
print('=' * 52) 
for pessoa in mulheres:
    print(f"Nome: {pessoa['Nome']}")

# Print dados gerais cadastrados 
print('=' * 52) 
print('DADOS GERAIS DOS CADASTRADOS'.center(52))
print('=' * 52)


print(f'Pessoas cadastradas: {quantia_pessoas}')
print(f'A media do grupo e: {media_idades}')


# Pessoas cadastradas acima da media de idade 
print('=' * 52) 
print('PESSOAS CADASTRADAS ACIMA DA MEDIA'.center(52))
print('=' * 52)

for pessoa in acima_da_media:
    print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}")


# fim programa
print('=' * 52)   
print('PROGRAMA ENCERRADO')
