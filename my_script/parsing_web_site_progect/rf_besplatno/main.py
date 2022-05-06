from get_url_ad import list_link_ad
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = True
    return options

def good_tel(tel):
    tel = tel.split()
    tel[0] = '7'
    tel = ''.join(tel)
    return tel

def write_csv(data):
    with open('rf_besplatno.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['tel']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_phone(browser):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located
            ((By.ID, 'phone-link2'))
        )
        browser.find_element(By.ID, 'phone-link2').click()
        tel = good_tel(browser.find_element(By.ID, 'phone-link2').text.strip())
    except:
        tel = 'none'
    finally:
        data = {'tel': tel}
        write_csv(data)
        print(f'Номер: {tel} >>> уже в CSV-файле!')

def main():
    browser = webdriver.Firefox(options=options())

    for i in list_link_ad:
        browser.get(i)
        try:
            get_phone(browser)
        except Exception as ex:
            print(ex)

    browser.close()
    browser.quit()

if __name__ == '__main__':
    main()

