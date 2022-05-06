import time
import pickle
from selenium import webdriver

def option():
    option = webdriver.FirefoxOptions()
    #отключаем флаг обнаружения бота
    option.set_preference('dom.webdriver.enabled', False)
    #отключаем показ уведомлений
    option.set_preference('dom.webnotifications.enabled', False)
    #отключаем все звуки
    option.set_preference('media.volume_scale', '0.0')
    #запускаем браузер фоном (флаг True)
    option.headless = False
    return option

browser = webdriver.Firefox(options=option())
browser.get('https://vk.com')
for cookie in pickle.load(open('vk_cooki', 'rb')):
    browser.add_cookie(cookie)
browser.refresh()

print('Я подгрузил куки!')

