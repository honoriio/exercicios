nome_completo = str(input('Informe seu nome completo : '))

palavras = nome_completo.split()

if len(palavras) >= 2:
    primeiro_nome = palavras[0]
    ultimo_nome = palavras[-1]

    print('Nome Completo : {}'.format(nome_completo))
    print('Primeiro Nome : {}'.format(primeiro_nome))
    print('Ultimo   Nome : {}'.format(ultimo_nome))
else:
    print('O nome inserido esta incompleto. Por favor Informe um nome valido.')
