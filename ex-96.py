import time

def contador():
    print('=' * 30)
    print('CONTADOR'.center(30))
    print('=' * 30)

    for i in range(1, 11):
        print(i)
        time.sleep(0.4)
        
    print('-' * 30)
    for j in range(10, 0, -2):
        print(j)
        time.sleep(0.4)
    print('=' * 30)


def contador2(v1, v2, passo):
    if passo == 0:
        passo = 1
        
    if v1 <= v2:
        for p in range(v1, v2 + 1, passo):
            print(p)
            time.sleep(0.4)
    else:
        for p in range(v1, v2 - 1, -passo):
            print(p)
            time.sleep(0.4)


contador()

v1 = int(input('Valor inicial: '))
v2 = int(input('Valor final: '))
passo = int(input('Passo: '))
print('-' * 30)

contador2(v1, v2, passo)
