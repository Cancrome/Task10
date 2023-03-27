"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess

ping= ''

links = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(links, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping += line.decode('cp866')

links2 = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(links2, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping += line.decode('cp866')

print(ping.encode('utf-8').decode('utf-8'))
