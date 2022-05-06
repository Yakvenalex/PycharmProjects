import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
browser = webdriver.Firefox(options=option)
browser.get('https://www.youtube.com')
time.sleep(3)

x_pa_1 = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer'
button = browser.find_element(By.XPATH, x_pa_1).click()
x_pa_2 = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
browser.find_element(By.XPATH, x_pa_2).send_keys('mr.mnogo@gmail.com')
x_pa_3 = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
browser.find_element(By.XPATH, x_pa_3).click()
