import requests
url = "http://pudim.com.br/"
try:
    respose = requests.get(url)
    print('=' * 52)
    print('\033[32mO site pudim esta disponivel!\033[0m'.center(52))
    print('=' * 52)
except requests.exceptions.RequestException:
    print('=' * 52)
    print('\033[31mO site Pudim não está disponivel.\033[0m'.center(52))
    print('=' * 52)

finally:
    print('\033[34mVOLTE SEMPRE QUE PRECISAR!\033[0m'.center(52))
    print('=' * 52)
