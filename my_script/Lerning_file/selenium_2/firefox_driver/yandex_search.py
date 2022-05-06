from selenium import webdriver
from selenium.webdriver.common.by import By
from actrises_rf import list_actris
import csv
import time

def write_csv(data):
    with open('big_actris.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    return options

def get_data(browser):
    time.sleep(5)
    result = browser.find_element(By.ID, 'search-result').find_elements(By.TAG_NAME, 'li')[0:1]
    for i in result:
        link = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
        name = i.find_element(By.TAG_NAME, 'h2').find_element(By.TAG_NAME, 'span').text
        data = {'name': name, 'link': link}

        write_csv(data)

def main():
        browser = webdriver.Firefox(options=options())
        browser.get('https://yandex.ru/search/')
        time.sleep(3)
        for l in list_actris:
            browser.find_element(By.XPATH, '/html/body/header/div/div/div[3]/form/div[1]/span/span/input').send_keys(f'{l}')
            time.sleep(2)
            browser.find_element(By.XPATH, '/html/body/header/div/div/div[3]/form/div[2]/button').click()
            get_data(browser)
            browser.find_element(By.XPATH, '/html/body/header/div/div/div[3]/form/div[1]/span/span/span[1]').click()
            time.sleep(5)

if __name__ == '__main__':
    main()