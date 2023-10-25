frase = str(input('Digite uma frase : '))

letra = "a"

frequencia = 0
primeira_ocorrencia = None
ultima_ocorrencia = None

for i in range(len(frase)):
    if frase[i] == letra:
        frequencia += 1
        if primeira_ocorrencia is None:
            primeira_ocorrencia = i
        ultima_ocorrencia = i
if frequencia > 0:
    print('A letra "A" aparece {} vez(es) na frase informada.'.format(frequencia))
    print('A primeira ocorrencia está na posição {}'.format(primeira_ocorrencia))
    print('A ultima ocorrência está na posição {}'.format(ultima_ocorrencia))
else:
    print('A letra "A" Não foi encontrada na Frase.')
