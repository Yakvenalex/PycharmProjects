from selenium import webdriver
import time
from fake_useragent import UserAgent

ua = UserAgent()

options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', ua.random)

url = 'http://whatsmyuseragent.org/'
browser = webdriver.Firefox(options=options)

try:
    browser.get(url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
