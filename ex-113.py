def leiaInt():
    import time
    while True:
        print('=' * 62)
        inteiro = input('Digite um valor inteiro: ').replace(',', '.')
        try:
            return int(inteiro)
        except ValueError:
            print('\033[31mTivemos problemas com os tipos de dados que você digitou.\033[0m')
            print('=' * 62)
            print('\033[32mREINICIANDO O PROGRAMA!\033[0m'.center(52))
            time.sleep(1)
        except KeyboardInterrupt:
            inteiro = 0
            print('O usuário decidiu não informar mais o número.')
            break  # Interrompe o loop ao receber KeyboardInterrupt
        except Exception as erro:
            print(f'O erro encontrado foi {erro}')
            print('=' * 62)
            print('\033[32mREINICIANDO O PROGRAMA!\033[0m'.center(52))
            time.sleep(1)
        



def leiaFloat():
    import time
    while True:
        print('=' * 62)
        real = input('Digite um valor Real: ').replace(',', '.')
        try:
            return float(real)
        except ValueError:
            print('\033[31mTivemos problemas com os tipos de dados que você digitou.\033[0m')
            print('=' * 62)
            print('\033[32mREINICIANDO O PROGRAMA!\033[0m'.center(52))
            time.sleep(1)
        except KeyboardInterrupt:
            print('\033[31mO usuário decidiu não informar mais o número.\033[0m')
            real = 0
            break  # Interrompe o loop ao receber KeyboardInterrupt
        except Exception as erro:
            print(f'O erro encontrado foi {erro}')
            print('=' * 62)
            print('\033[32mREINICIANDO O PROGRAMA!\033[0m'.center(52))
            time.sleep(1)
    
            
try:
    inteiro = leiaInt()
    real = leiaFloat()
    print('=' * 62)
    print(f'\033[32mO valor inteiro digitado foi {inteiro} e o real foi {real}\033[0m')
    print('=' * 62)
except KeyboardInterrupt:
    print('\033[31mO usuário decidiu não informar mais o número.\033[0m')
    print('=' * 62)
