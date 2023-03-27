"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

link1 = 'yandex.ru'
ARGS = ['ping', link1]
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print('YANDEX: ')
for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


print('_' * 20)
print('YOUTUBE: ')
link2 = 'youtube.com'
ARGS = ['ping', link2]
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
