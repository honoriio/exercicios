# importando o modulo datatime
from datetime import datetime

# criando o dicionario
cadastro = dict()

# obtendo ano atual
ano_atual = datetime.now().year

# Tela de apresentação
print('=' * 52)
print('VERIFICADOR DE APOSENTADORIA'.center(52))
print('=' * 52)

# entrada de dados atravez do usuario
cadastro['Nome'] = str(input('Nome: '))
cadastro['Ano de nascimento'] = int(input('Ano de nascimento: '))

# calculo de idade com base no ano de nascimento e ano atual (falta precisão)
cadastro['Idade'] = ano_atual - cadastro['Ano de nascimento']

# Verificação de CTPS
validacao = str(input('Possui CTPS? [S/N]: ')).upper()

# Verificando se o mesmo tem CTPS, caso tiver o usuario tera que inserir mais dados, se não o programa finalizara.
if validacao == 'N':
    print('=' * 52)
    print('DADOS CADASTRAIS'.center(52))
    print('=' * 52)
    for chave, valor in cadastro.items():
        print(f'{chave}: {valor}')
        print('-' * 52)
    print('=' * 52)
else:
    cadastro['CTPS'] = int(input('Número CTPS: '))
    cadastro['Contratacao'] = int(input('Ano de Contratação: '))
    cadastro['Salario'] = float(input('Salario R$: '))

    # Anos de trabalho necessario para se aposentar.
    cadastro['Anos para aposentar'] = 35

    # calculando com quantos anos o usuario podera se aposentar.
    cadastro['Anos trabalhados'] = ano_atual - cadastro['Contratacao']
    cadastro['Anos Restantes'] = cadastro['Anos para aposentar'] - cadastro['Anos trabalhados']
    cadastro['Idade aposentadoria'] = cadastro['Idade'] + cadastro['Anos Restantes']
    cadastro['Ano da aposentadoria'] = ano_atual + cadastro['Anos Restantes']

# Exibindo os dados cadastrais de forma formatada usando f-strings
print('=' * 52)
print('DADOS CADASTRAIS'.center(52))
print('=' * 52)

for chave, valor in cadastro.items():
    if chave == 'Salario':
        # Formatando o salário com duas casas decimais
        print(f'{chave.capitalize():<20}: R$ {valor:.2f}')
    else:
        print(f'{chave.capitalize():<20}: {valor}')

print('=' * 52)
