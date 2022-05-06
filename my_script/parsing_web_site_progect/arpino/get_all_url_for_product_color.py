import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = True
    return options

browser = webdriver.Firefox(options=options())

shpon_l = []
emal_spon_l = []
mdf_l = []

url = input('Вставь ссылку: ')
browser.get(url)

print('Начинаю сканирование страницы...')

# получаю список ссылок на шпон
pattern = '/html/body/content/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[{}]'
for i in range(1, 11):
    xp = pattern.format(str(i))
    try:
        browser.find_element(By.XPATH, xp).click()
        photo = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[3]/a').get_attribute('href')
        shpon_l.append(browser.current_url)
    except:
        pass

# получаю список ссылок на эмаль по шпону
pattern = '/html/body/content/div[1]/div[5]/div[2]/div[2]/div[2]/div[2]/div[{}]'
for i in range(1, 11):
    xp = pattern.format(str(i))
    try:
        browser.find_element(By.XPATH, xp).click()
        photo = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[3]/a').get_attribute('href')
        emal_spon_l.append(browser.current_url)
    except:
        pass

# получаю список ссылок на мдф
pattern = '/html/body/content/div[1]/div[5]/div[2]/div[2]/div[3]/div[2]/div[{}]'
for i in range(1, 11):
    xp = pattern.format(str(i))
    try:
        browser.find_element(By.XPATH, xp).click()
        photo = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[3]/a').get_attribute('href')
        mdf_l.append(browser.current_url)
    except:
        pass

num = len(shpon_l) + len(emal_spon_l) + len(mdf_l)

print(f'Сканирование страницы завершено. Я скачаю тебе {num} фото')
print("Приступаю к загрузки фото на диск С")

browser.close()
browser.quit()