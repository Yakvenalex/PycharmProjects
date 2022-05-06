import fake_useragent
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

storage_number = 1
link = f'https://zastavok.net/'

responce = requests.get(f'{link}/{storage_number}').text
soup = BeautifulSoup(responce,'lxml')
block = soup.find('div', class_ = 'block-photo')
all_image = block.find_all('div', class_ = 'short_full')

for image in all_image:
    image_link = image.find('a').get('href')
    download_storage = requests.get(f'{link}/{image_link}').text
    print(download_storage)