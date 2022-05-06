import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

user = UserAgent().random
header = {'user-agent': user}


link = 'https://browser-info.ru/'
responce = requests.get(link, headers=header).text

soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id='tool_padding')

check_js = block.find('div', id = 'javascript_check')
result_js = check_js.find_all('span')[1].text

check_flash = block.find('div', id = 'flash_version')
result_flash = check_flash.find_all('span')[1].text

check_user = block.find('div', id = 'user_agent').text

print(f'Статус Javascript: {result_js}')
print(f'Статус Flash: {result_flash}')
print(check_user)