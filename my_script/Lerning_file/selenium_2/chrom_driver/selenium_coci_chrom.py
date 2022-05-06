from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from auch_data import *
import pickle

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)

stealth(browser, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32", webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)
url = "https://bot.sannysoft.com/"
browser.get(url)

time.sleep(5)
browser.find_element(By.XPATH, '/html/body/div[10]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/button[1]').click()
time.sleep(2)
browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/section/div/div/div/input').send_keys(login + Keys.ENTER)
time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input').send_keys(password + Keys.ENTER)
time.sleep(15)
pickle.dump(browser.get_cookies(), open(f'{login}_cookies_vk', 'wb'))

# browser.get(url)
# time.sleep(6)
# browser.delete_all_cookies()
# for cookie in pickle.load(open('mr.mnogo@gmail.com_cookies_vk', 'rb')):
#     browser.add_cookie(cookie)
# time.sleep(25)
# browser.refresh()
