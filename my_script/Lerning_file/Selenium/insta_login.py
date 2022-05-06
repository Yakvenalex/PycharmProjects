import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
browser = webdriver.Firefox(options=option)
browser.get('https://www.instagram.com/accounts/login/')


button = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()

time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input').click()

time.sleep(1)
browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys('sait_admin')
time.sleep(1)
browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input').click()
time.sleep(1)
browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys('75251qqq')
time.sleep(1)
browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]').click()
time.sleep(5)
browser.get('https://www.instagram.com/parfumbuyer/')
time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]').click()
time.sleep(5)
searchBtn = browser.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div')

time.sleep(3)

#105 кликов - это примерно 1000
html = browser.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
n = 0
for i in range(160):
    html.send_keys(Keys.END)
    n += 1
    print(f'Я нажал на клавишу END: {n} раз(а)!')
    time.sleep(5)