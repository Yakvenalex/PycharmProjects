from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

print('Начинаю сбор ссылок на объявления. Это может занять пару минут...')

l = []

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = False
    return options

browser = webdriver.Firefox(options=options())

pattern = 'https://www.avito.ru/rossiya/detskaya_odezhda_i_obuv/platya_i_yubki-dlya_devochek-ASgBAgICAkTkAuwL5gL6Cw?cd=1&p={}'

for i in range(1, 3):
    url = pattern.format(str(i))
    browser.get(url)

    items = browser.find_elements(By.CLASS_NAME, 'iva-item-titleStep-pdebR')

    for i in items:
        link = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
        l.append(link)

browser.close()
browser.quit()

print("Сканирование завершено успешно")
print(f'Я сохранил ссылки на {len(l)} объявлений')
print(l)
print('Приступаю к сбору нужных данных с каждого объявления...')

