from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    return options

def main():
        browser = webdriver.Firefox(options=options())
        browser.get('https://yandex.ru/')
        time.sleep(3)
        browser.find_element(By.XPATH, '//*[@id="text"]').send_keys('елена яковлева инстаграмм' + Keys.ENTER)
        time.sleep(5)
        result = browser.find_element(By.ID, 'search-result').find_elements(By.TAG_NAME, 'li')[0:2]
        for i in result:
            link = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(link)


if __name__ == '__main__':
    main()