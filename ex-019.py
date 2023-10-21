import random

nome1 = input('Informe o nome do Primeiro aluno : ')
nome2 = input('Informe o nome do Segundo  aluno : ')
nome3 = input('Informe o nome do terceiro aluno : ')
nome4 = input('Informe o nome do quarto   aluno : ')

nomes = [nome1, nome2, nome3, nome4]
random.shuffle(nomes)

print('A ordem da apresentação será a sequinte \n {}'.format(nomes))
