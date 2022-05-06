from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = False
    return options

def get_data(browser):
    html = browser.page_source
    print(html)
def main():
    browser = webdriver.Firefox(options=options())
    browser.get('https://moskva.doski.ru/tekstilschiki/primu-v-dar-veschi-na-podrostka-devochku-13-let-msg4842060.htm?cat=653&mtp=0&plc=1')
    get_data(browser)

if __name__ == '__main__':
    main()