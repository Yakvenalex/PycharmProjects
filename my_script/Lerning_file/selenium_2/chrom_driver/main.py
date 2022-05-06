from fake_useragent import UserAgent
from selenium import webdriver
import time

ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={ua.random}')

url = 'http://whatsmyuseragent.org/'
browser = webdriver.Chrome(options=options)

try:
    browser.get(url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
