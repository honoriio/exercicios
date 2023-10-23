nome = input('Qual é o seu nome completo? : ')

print(nome.upper())
print(nome.lower())


contagem = 0
for caracter in nome:
    if caracter != " ":
        contagem += 1
print(f'O total de caracteres sem espaços é: {contagem}')


palavras = nome.split()
primeiro_nome = palavras[0]
comprimento = len(primeiro_nome)
print(f'O primeiro nome tem {comprimento} letras')
