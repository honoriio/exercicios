from utilidades.moedas import moedas
from utilidades.dados import dados


valor = dados.leiaDinheiro('Digite o preco: R$')
moedas.resumo(valor, 0.80, 0.35)
