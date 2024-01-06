
# Listas e dicionariosaaaaaaa
pessoas = list()

# Apresentação
print('=' * 52)
print('CADASTRO DE PESSOAS'.center(52))
print('=' * 52)

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    print('-' * 52)

    pessoa = {'Nome' : nome, 'Idade' : idade, 'Sexo' : sexo}
    pessoas.append(pessoa)

    decisao = input('Deseja continuar [S/N]: ').upper()
    print('-' * 52)

    if decisao == 'N':
        break
    
print('=' * 52)
print('PESSOAS CADASTRADAS'.center(52))
print('=' * 52)
for pessoa in pessoas:
    
    print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Sexo: {pessoa['Sexo']}")
    print('-' * 52)

print('=' * 52)   
print('PROGRAMA ENCERRADO')
