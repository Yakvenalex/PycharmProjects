import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from avito_auch import *
from get_url_ad import l
import base64
import os

def write_csv(data):
    with open('avito.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'phone']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def find_name(browser):
    time.sleep(3)
    name = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div/div[4]/div/div[1]/div[1]/div[1]/div/a').text
    return name

def good_number(text):
    text[0] = '7'
    text = '-'.join(text)
    text = text.split('-')
    text = ''.join(text)
    return text

def good_pic(url):
    url = url.split(',')[1]
    return url

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = False
    return options

def get_photo_number(browser, num):
    os.chdir('photo_n')
    time.sleep(5)
    try:
        browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div/div[3]/div/div[2]/div/div/span/span/button').click()
        time.sleep(2)
        src = good_pic(browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div/div[3]/div/div[2]/div/div/span/span/button/span/img').get_attribute('src'))
    except:
        src = not_number

    base64_img_bytes = src.encode('utf-8')

    with open(f'{num}_photo.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)
        print(f'Фотография: {num}_photo.png сохранена успешно!')

    os.chdir('..')

def login_avito(browser):
    time.sleep(5)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[1]/div[2]/a').click()
    browser.find_element(By.NAME, 'login').send_keys(login)
    browser.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(3)
    browser.find_element(By.NAME, 'submit').click()
    time.sleep(4)

def scan_number(name):
    os.chdir('photo_n')
    li = os.listdir()

    if len(li) == 1:
        img = Image.open(li[-1])
    else:
        img = Image.open(li[-2])

    pytesseract.pytesseract.tesseract_cmd = scaner
    phone = good_number(pytesseract.image_to_string(img).strip().split())

    data = {'name': name, 'phone': phone}
    write_csv(data)
    print(f'Данные {data} записаны!')
    os.chdir('..')

def main():
    num = 999
    browser = webdriver.Firefox(options=options())
    browser.get('https://www.avito.ru/samara/detskaya_odezhda_i_obuv/plate_dlya_devochki_92_razmer_2358437583?slocation=621540')
    login_avito(browser)
    for i in l:
        time.sleep(5)
        num += 1
        browser.get(i)
        name = find_name(browser)
        get_photo_number(browser, num)
        scan_number(name)

if __name__ == '__main__':
    main()