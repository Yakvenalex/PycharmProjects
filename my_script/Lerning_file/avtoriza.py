import fake_useragent
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

session = requests.Session()


link = 'https://www.cyberforum.ru/log-in.php'
user = UserAgent().random

header = {
    'user-agent':user
}

data = {
    'req_username':'mr.mnogo@gmail.com',
    'req_password':'75251qqq'
}

responce = session.post(link, data = data, headers = header).text
profile_info = 'https://www.cyberforum.ru/members/1962453.html'
profile_responce = session.get(profile_info, headers = header).text

print(profile_responce)