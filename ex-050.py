a = 2  # Primeiro termo
r = 3  # Razão
n = 5  # Número de termos desejados

progressao_aritmetica = []
for i in range(n):
    termo = a + i * r
    progressao_aritmetica.append(termo)

print(progressao_aritmetica)
