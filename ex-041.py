a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

# Verificar se é possível formar um triângulo
if a + b > c and a + c > b and b + c > a:
    # Verificar o tipo de triângulo
    if a == b == c:
        print("É um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é possível formar um triângulo com essas medidas.")