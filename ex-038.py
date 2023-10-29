import datetime
nasc = int(input('Informe seu ano de nascimento : '))

# Uso do modulo datetime
data_atual = datetime.datetime.now()
ano_atual = data_atual.year

# Calculo para saber a idade atual da pessoa
idade = (ano_atual - nasc)

# valores minimos e maximos para o alistamento.
alistamento_idade_minima = 18
alistamento_idade_maxima = 45

# Calculos para saber o tempo que falta para o alistamento ou se o mesmo ja foi exedido.
tempo_restante = (alistamento_idade_minima - idade)
tempo_restante_18 = (alistamento_idade_maxima - idade)

# checagem de dados usando condições condcionais.
if idade <= 18:
    print("Você ainda não pode se alistar para o exercito, você podera fazer isso daqui a {} anos".format(tempo_restante))
elif (idade > 18) or (idade == 45):
    print('Você Já pode fazer o alistamento obrigatorio, você tem ate os seus {} anos de idade.'.format(alistamento_idade_maxima))
elif idade > 45:
    print('Você já ultrapassou a idade limite para o alistamento obrigatorio.')
elif idade <= 0:
    print('Formato invalido, por favor insira um formato valido.')
