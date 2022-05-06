from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

l = []

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = False
    return options

browser = webdriver.Firefox(options=options())
pattern = 'https://www.farpost.ru/children/clothes-boots/?condition%5B%5D=used&page={}'
pattern_x = '/html/body/div[3]/div[4]/div/form/table/tbody/tr[3]/td/div[1]/table[1]/tbody/tr[{}]/td/div/div/div[2]/div[2]/div[1]/a'

for i in range(1, 3):
    url = pattern.format(str(i))
    browser.get(url)
    time.sleep(5)

    for y in range(2, 52):
        xpatch = pattern_x.format(str(y))
        link = browser.find_element(By.XPATH, xpatch).get_attribute('href')
        l.append(link)
        print(link)
print(l)
print(len(l))

browser.close()
browser.quit()


