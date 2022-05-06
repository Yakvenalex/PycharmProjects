from selenium import webdriver
from selenium.webdriver.common.by import By
from actrises_rf import list_actris
from selenium.webdriver.common.keys import Keys
import csv
import time

def follower(x):
    if '.' in x:
        if 'K' in x:
            K = '00'
            x = x.replace('K', '00')
            x = x.replace('.', '')
            return x
        elif 'M' in x:
            M = '00000'
            x = x.replace('M', '00000')
            x = x.replace('.', '')
            return x
    else:
        if 'K' in x:
            x = x.replace('K', '000')
            return x
        elif 'M' in x:
            M = '00000'
            x = x.replace('M', '000000')
            return x
    return x

print(f'Я спарсил для тебя следующие имена: {list_actris}')

def good_name(name):
    name = " ".join(name)
    return name

def write_csv(data):
    with open('big_actris.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'followers', 'link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    return options

def get_data(browser):
    time.sleep(5)
    first = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div/ol/li[1]/div')
    link = first.find_element(By.TAG_NAME, 'a').get_attribute('href')
    name = good_name(first.find_element(By.TAG_NAME, 'a').text.split('\n')[1].split(" ")[0:2])
    try:
        followers = follower(browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div/ol/li[1]/div/div[3]/ul/li').text.split(' ')[1])
    except:
        followers = 'Нет данных!'

    data = {'name': name, 'followers': followers, 'link': link}
    print(f'{data} - данные записаны!')
    write_csv(data)

def main():
        browser = webdriver.Firefox(options=options())
        browser.get('https://search.yahoo.com/search;_ylt=AwrJ61bQ5mFiTo8AUJtXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3NmcARmcjIDc2ItdG9wBGdwcmlkA3NwQ3MyLkdXU01tM2g1a2UyT2p2VkEEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzIxBHF1ZXJ5AyVEMSU4MiVEMSU4MyVEMSU4MiUyMCVEMCVCMSVEMSU4MyVEMCVCNCVEMCVCNSVEMSU4MiUyMCVEMCVCOCVEMCVCQyVEMSU4RiUyMCVEMCVCMCVEMCVCQSVEMSU4MiVEMSU4MCVEMCVCOCVEMSU4MSVEMSU4QgR0X3N0bXADMTY1MDU4MzMzMg--?p=тут+будет+имя+актрисы&fr2=sb-top&fr=sfp')
        time.sleep(3)
        for l in list_actris:
            browser.find_element(By.ID, 'sbq-clear').click()
            browser.find_element(By.ID, 'yschsp').send_keys(f'{l}' + Keys.ENTER)
            get_data(browser)
        browser.close()
        browser.quit()

if __name__ == '__main__':
    main()