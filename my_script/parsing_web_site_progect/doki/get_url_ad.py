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
pattern = 'https://www.doski.ru/cat-detskiy-mir/detskaya-odezhda-obuv/?page={}'
pattern_x = '/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[{}]/td[2]/a[1]'

for i in range(56, 70):
    url = pattern.format(str(i))
    browser.get(url)
    time.sleep(3)

    for y in range(1, 21):
        xpatch = pattern_x.format(str(y))
        link = browser.find_element(By.XPATH, xpatch).get_attribute('href')
        l.append(link)
        print(link)

print(l)
print(len(l))

browser.close()
browser.quit()
