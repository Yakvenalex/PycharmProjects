from selenium import webdriver
from fake_useragent import UserAgent

option = webdriver.FirefoxOptions()
option.set_preference('general.useragent.override', UserAgent().random)
browser = webdriver.Firefox(options=option)
browser.get('http://whatsmyuseragent.org/')

