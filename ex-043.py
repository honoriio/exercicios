produto = float(input('Informe o valor do produto R$'))
forma_pagamento = str(input('Informe a forma de pagamanto : '))

if forma_pagamento.startswith("dinheiro") or forma_pagamento.startswith("chegue"):
    desconto = (produto * 10) / 100
    produto_desconto = (produto - desconto)
    print('Forma de pagamento: {}. valor do produto R${:.2f}'.format(forma_pagamento, produto))
    print("Você recebeu 5% de desconto o valor a pagar é de R${}".format(produto_desconto))

elif forma_pagamento.startswith("cartao"):
    cartao = input('O valor sera pago a vista ou parcelado? :')

    if cartao.startswith("a vista"):
        desconto = (produto * 5) / 100
        produto_desconto = (produto - desconto)
        print('Forma de pagamento: {}. valor do produto R${:.2f}'.format(forma_pagamento, produto))
        print("Você recebeu 5% de desconto o valor a pagar é de R${:.2f}".format(produto_desconto))

    elif cartao.startswith("parcelado"):
        parcelas = int(input('Quantas vezes deseja parcelar? : '))

        if parcelas == 2:
            valor_parcelado = (produto / parcelas)
            print('Você escolheu parcelar em: {} vezes. Cada parcela será de R${:.2f}'.format(parcelas, valor_parcelado))
            print('Neste caso, não será possivel dar desconto.')

        elif parcelas > 2:
            juros = (produto * 20) / 100
            produto_juros = (produto + juros)
            valor_parcelado = (produto / parcelas)
            print('Você escolheu parcelar em {} vezes. Cada parela será de R${:.2f}'.format(parcelas, valor_parcelado))
            print('Neste caso tera um acrescimo de 20% no valor do produto, ficando em R${:.2f}'.format(produto_juros))
        else:
            print('Número de parcelas inválido')
    else:
        print('Opção de pagamento não reconhecido para cartão.')
else:
    print('Forma de pagamento não reconhecida.')
