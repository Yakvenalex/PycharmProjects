from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from auch_data import *

url = 'https://vk.com'
browser = webdriver.Chrome()

try:
    browser.get(url)
    time.sleep(5)
    browser.find_element(By.XPATH, '/html/body/div[10]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/button[1]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/section/div/div/div/input').send_keys(login)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/button/div').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input').send_keys(password)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/button/div/span').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div[11]/div/div/div[2]/div[1]/div/nav/ol/li[1]/a/span[1]').click()
except Exception as ex:
    print(ex)
# finally:
#     browser.close()
#     browser.quit()
