from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from get_url_ad import l

def good_number(text):
    text[0] = '7'
    text = '-'.join(text)
    text = text.split('-')
    text = ''.join(text)
    return text

def write_csv(data):
    with open('farpost.csv', 'a', newline='', encoding="utf-8") as f:
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
    name = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/table/tbody/tr/td[1]/div/div[4]/div/div[1]/div/div[2]/div/div[1]/span').text
    browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/table/tbody/tr/td[1]/div/div[4]/div/div[1]/div/div[5]/div[1]/div/a').click()
    time.sleep(3)
    phone = good_number(browser.find_element(By.XPATH, '/html/body/div[7]/main/div/div[1]/div/div').text.split())
    data = {'name': name, 'phone': phone}
    write_csv(data)

def main():
    browser = webdriver.Firefox(options=options())
    for i in l:
        browser.get(i)
        try:
            get_data(browser)
            print('Все прошло успешно. Перехожу к следующему номеру')
        except:
            print('Что-то пошло не так. Проверь!')
            time.sleep(60)
        time.sleep(5)
    browser.close()
    browser.quit()

if __name__ == '__main__':
    main()