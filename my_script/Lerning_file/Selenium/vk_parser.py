import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

def option():
    option = webdriver.FirefoxOptions()
    option.set_preference('dom.webdriver.enabled', False)
    return option

browser = webdriver.Firefox(options=option())

def write_csv(data):
    with open('parfum_vk.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'state', 'city', 'link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def login_vk():
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div[10]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/button[1]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/section/div/div/div/input').send_keys('mr.mnogo@gmail.com')
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/div[1]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input').send_keys('q75251qqq')
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/button/div/span').click()

def vk_scroll():
    time.sleep(5)
    browser.get('https://vk.com/search?c[section]=people&c[group]=109624730')

    html = browser.find_element(By.TAG_NAME, 'html')

    n = 0
    for i in range(60):
        html.send_keys(Keys.END)
        n += 1
        print(f'Я клацнул на END {n} раз(f)')
        time.sleep(1)

    time.sleep(8)
    print('Я завершил скроллинг. Приступаю к записи')

def get_data():
    peoples = browser.find_element(By.XPATH, '//*[@id="results"]').find_elements(By.CLASS_NAME, 'info')
    p = len(peoples)

    print(f'Я для тебя нашел информацию на {p} подписчиков!')
    time.sleep(10)

    print(f'Приступаю к записи. Это займет пару минут!')

    for people in peoples:
        link = people.find_element(By.TAG_NAME, 'a').get_attribute('href')

        try:
            name = people.find_element(By.TAG_NAME, 'a').text
        except:
            name = people.find_element(By.CLASS_NAME, 'labeled name').find_element(By.TAG_NAME, 'a').text

        try:
            state = people.find_elements(By.CLASS_NAME, 'labeled')[1].text.split()[1]
        except:
            state = ''

        try:
            city = people.find_elements(By.CLASS_NAME, 'labeled')[1].text.split()[0][:-1]
        except:
            city = ''


        data = {'name': name, 'state': state, 'city': city, 'link': link}

        write_csv(data)

def main():
    browser.get('https://vk.com')
    login_vk()
    vk_scroll()
    get_data()
    print('Вся работа завершена успешно. Досвидания!')
    browser.quit()

if __name__ == '__main__':
    main()