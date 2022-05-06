from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from get_url_ad import l

def good_number(a):
    a = ''.join(a).split('(')
    a = ''.join(a).split(')')
    a = ''.join(a).split()
    a[0] = '7'
    a = ''.join(a)
    return a

def write_csv(data):
    with open('doki.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'phone']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = False
    return options

def get_data(browser):
    time.sleep(3)
    try:
        name = browser.find_element(By.XPATH, '/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td/b').text.strip().split(' ')[1]
    except:
        name = 'нет имени'

    try:
        browser.find_element(By.ID, 'phn').click()
        time.sleep(3)
        phone = browser.find_element(By.ID, 'phn').text
    except:
        phone = 'номер не найден!'
    data = {'name': name, 'phone': phone}
    print(data)
    write_csv(data)

def main():
    browser = webdriver.Firefox(options=options())

    for i in l:
        browser.get(i)
        get_data(browser)
        print('Все прошло успешно. Перехожу к следующему номеру')
    browser.close()
    browser.quit()

if __name__ == '__main__':
    main()