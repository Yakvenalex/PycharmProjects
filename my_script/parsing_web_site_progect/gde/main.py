from get_url_ad import my_link_list
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

print('Запускаю парсинг номеров через браузер FireFox')

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = False
    return options

def good_tel(tel):
    tel = tel.split()
    tel[0] = '7'
    tel = ''.join(tel)
    tel = tel.replace('(', '')
    tel = tel.replace(')', '')
    tel = tel.replace('-', '')
    return tel

def write_csv(data):
    with open('gde.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'tel']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_phone(browser):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located
            ((By.XPATH, '/html/body/div[1]/div[1]/div/div/div[4]/aside/ul/li[1]/noindex/div[1]/div'))
        )
        browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[4]/aside/ul/li[1]/noindex/div[1]/div').click()
        time.sleep(1)
        tel = good_tel(browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[4]/aside/ul/li[1]/noindex/div[1]/div/a').text.strip())
        name = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[4]/aside/ul/li[4]/table/tbody/tr/td/div[1]/span/a').text
    except:
        tel = 'none'
        name = 'none'
    finally:
        data = {'name': name, 'tel': tel}
        write_csv(data)
        print(f'Имя: {name}, Номер: {tel} >>> уже в CSV-файле!')

def main():
    browser = webdriver.Firefox(options=options())
    url = 'https://pushkin.gde.ru/c/myagkaya_igrushka_68409477.html'

    for url in my_link_list:
        browser.get(url)
        try:
            get_phone(browser)
        except Exception as ex:
            print(ex)
            print('Что-то полшло не так :( Закрываю браузер')

    browser.close()
    browser.quit()

if __name__ == '__main__':
    main()

