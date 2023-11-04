def e_primo(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    elif numero <= 3:
        return True  # 2 e 3 são primos

    if numero % 2 == 0:
        return False  # Números pares maiores que 2 não são primos

    for divisor in range(3, int(numero**0.5) + 1, 2):
        if numero % divisor == 0:
            return False  # O número é divisível por um número diferente de 1 e ele mesmo

    return True  # Se não houver divisores encontrados, o número é primo

numero = int(input("Digite um número para verificar se é primo: "))

if e_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
