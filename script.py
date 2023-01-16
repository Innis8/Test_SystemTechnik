import re
import requests
import socket


URL = 'https://sstmk.ru/'


phone_regex = re.compile(r'''(
                        (8\s\(\d{3}\))?
                        (\s|-)
                        (\d{3})
                        (\s|-)
                        (\d{2})
                        (\s|-)
                        (\d{2}))''', re.VERBOSE)

print(f'Сайт компании: {URL}\n')
print('Статус работы сайта:')
try:
    response = requests.head(URL)
except Exception as e:
    print(f'NOT OK: {str(e)}\n')
else:
    if response.status_code == 200:
        print('OK\n')
    else:
        print(f'NOT OK: HTTP response code {response.status_code}\n')


url='sstmk.ru'
print(f'IP-адрес сайте: {socket.gethostbyname(url)}\n')


page_data = requests.get(URL)
page_html = str(page_data.content)

matches = []
for groups in phone_regex.findall(page_html):
    phone_numbers = '-'.join(
        [groups[1], groups[3], groups[5], groups[7]]
    ).replace(' ','').replace(')-',')').replace('8(','+7(')
    matches.append(phone_numbers)
print('Телефон компании:')
print('\n'.join(list(set(matches))))
