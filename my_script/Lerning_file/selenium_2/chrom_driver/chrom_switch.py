from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def options():
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        return options

def stels(browser):
        stealth(browser,
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
                languages=["ru-RU", "ru"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)

def main():
        browser = webdriver.Chrome(options=options())
        stels(browser)
        browser.get('https://www.avito.ru/rossiya/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw')
        items = browser.find_elements(By.CLASS_NAME, 'iva-item-titleStep-pdebR')
        time.sleep(7)
        items[40].click()
        browser.switch_to.window(browser.window_handles[1])
        price = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div/div[1]/div/div/div/div/span/span/span[1]').text
        print(price)
        adress = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/span').text
        print(adress)
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(500)
if __name__ == '__main__':
    main()