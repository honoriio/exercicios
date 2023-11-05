pessoas = []
soma_idades = 0
idade_homem_mais_velho = -1
nome_homem_mais_velho = None
mulheres_menos_de_20 = 0

for i in range(4):
    print('-' * 45)
    print('{}° Pessoa:'.format(i + 1))
    nome = input('Informe o nome da {}° pessoa:'.format(i + 1))
    idade = int(input('Informe a idade da {} pessoa: '.format(i + 1)))
    sexo = input('Informe o sexo da {} pessoa (M/F): '.format(i + 1)).upper()

    pessoa = {'Nome': nome, 'Idade': idade, 'Sexo': sexo}
    pessoas.append(pessoa)

    soma_idades += idade  # calcule a media

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1
media_idades = soma_idades / len(pessoas)  # calcula a media da idade

print('\nDados das pessoas coletados:')
for i, pessoa in enumerate(pessoas, start=1):
    print(f'{i}ª pessoa - Nome: {pessoa["Nome"]}, Idade: {pessoa["Idade"]}, Sexo: {pessoa["Sexo"]}')

print('\nA média das idades do grupo é: {:.2f}'.format(media_idades))

if nome_homem_mais_velho:
    print('O homem mais velho é: {}'.format(nome_homem_mais_velho))
else:
    print('Nenhum homem foi informado.')

print('Número de mulheres com menos de 20 anos: {}'.format(mulheres_menos_de_20))
