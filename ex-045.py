import time
import emoji
print('=' * 32)
print('       CONTAGEM REGRESSIVA')
print('=' * 32)


for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('-' * 32)
print(emoji.emojize(':fireworks:' * 14))
print('-' * 32)
