from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from multiprocessing import Pool

urls_list = ['https://ru.stackoverflow.com', 'http://instagram.com', 'http://vk.com']

def options():
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        return options

def get_good_url(url):
        url = url.split('//')[1]
        return url

def get_data(url):
        browser = webdriver.Chrome(options=options())
        browser.get(url=url)
        time.sleep(5)
        browser.get_screenshot_as_file(f'media/{get_good_url(url)}.png')

if __name__ == '__main__':
    p = Pool(processes=3)
    p.map(get_data, urls_list)