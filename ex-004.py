algo = input(' Digite algo : ')

print('{} e alfabetico? :'.format(algo), algo.isalpha())
print('{} e Numerico? :'.format(algo), algo.isnumeric())
print(' {} e Alfanumerico? :'.format(algo), algo.isalnum())
print('{} e codigo ascii? :'.format(algo), algo.isascii())
print(' {} e Digito? :'.format(algo), algo.isdigit())
print(' {} e Decimal? :'.format(algo), algo.isdecimal())
print(' {} e Identificador? :'.format(algo), algo.isidentifier())
print(' {} e Imprimivel? :'.format(algo), algo.isprintable())
print(' {} e Minusculo? :'.format(algo), algo.islower())
print(' {} e Um Espaço? :'.format(algo), algo.isspace())
print(' {} e um Titulo? :'.format(algo), algo.istitle())
print(' {} e Maiuscula? :'.format(algo), algo.isupper())