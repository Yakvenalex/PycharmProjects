from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from auch_data import *
import pickle

browser = webdriver.Firefox()

#Авторизуемся и получаем куки

# browser.get(url)
# time.sleep(5)
# browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
# time.sleep(2)
# browser.find_element(By.NAME, 'username').send_keys(login)
# time.sleep(2)
# browser.find_element(By.NAME, 'password').send_keys(password + Keys.ENTER)
# time.sleep(15)
# pickle.dump(browser.get_cookies(), open(f'{login}_cookies_vk', 'wb'))
# # time.sleep(10)
# browser.close()
# browser.quit()

#Импортируем куки (чтоб не нужно было логин и пароль вводить)

browser.get('https://www.instagram.com/')
time.sleep(5)
browser.delete_all_cookies()
for cookie in pickle.load(open('sait_admin_cookies_vk', 'rb')):
    browser.add_cookie(cookie)
time.sleep(10)
browser.refresh()