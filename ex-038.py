import datetime

ano_nasc = int(input('Informe o ano do seu nascimento: '))

agora = datetime.datetime.now()
formatado = "%d/%m/%Y"
data_formatada = agora.strftime(formatado)
print(data_formatada)
