from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from auch_data import *

url = 'https://www.instagram.com/'
browser = webdriver.Firefox()

browser.get(url)
time.sleep(5)
browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
time.sleep(2)
browser.find_element(By.NAME, 'username').send_keys(login)
time.sleep(2)
browser.find_element(By.NAME, 'password').send_keys(password + Keys.ENTER)
time.sleep(2)
