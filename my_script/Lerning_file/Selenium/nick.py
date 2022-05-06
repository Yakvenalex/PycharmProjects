from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def option():
    option = webdriver.FirefoxOptions()
    #отключаем флаг обнаружения бота
    option.set_preference('dom.webdriver.enabled', False)
    #отключаем показ уведомлений
    option.set_preference('dom.webnotifications.enabled', False)
    #отключаем все звуки
    option.set_preference('media.volume_scale', '0.0')
    #запускаем браузер фоном (флаг True)
    option.headless = True
    return option

def write_csv(data):
    with open('nik.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_data(browser):
    button_xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    browser.find_element(By.XPATH, button_xpath).click()

    link = browser.find_element(By.ID, 'register').get_attribute('href')[37:]

    data = {'link': link}
    print(link)
    write_csv(data)

def main():
    browser = webdriver.Firefox(options=option())
    browser.get('https://mynickname.com/generate')
    n = 0
    while n != 10:
        n += 1
        get_data(browser)

    browser.quit()

if __name__ == '__main__':
    main()