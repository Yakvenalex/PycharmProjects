import time
import pickle
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.cyberforum.ru/')
for cookie in pickle.load(open('sessio', 'rb')):
    browser.add_cookie(cookie)
browser.refresh()
