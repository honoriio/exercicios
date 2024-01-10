from datetime import datetime


def voto():
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento

    if idade <= 0:
        print('ANO DE NASCIMENTO INSERIDO ERRADO.')
    elif idade <= 15:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    print('=' * 62)
    print('PROGRAMA FINALIZADO'.center(62))
    print('=' * 62)


def tela():
    print('=' * 62)
    print('VERIFICADOR DE VOTOS.'.center(62))
    print('=' * 62)



tela()
nascimento = int(input('Informe o ano de nascimento: '))
voto()
