from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from get_info import keyss, name_photo
from selenium.webdriver.common.keys import Keys

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = False
    return options

def arpino_login(browser):
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/form/div[1]/div/input').send_keys('admin')
    browser.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/form/div[2]/div/input').send_keys(
        'dk20flk2cm200flkd')
    browser.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/form/div[3]/button').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/button').click()
    time.sleep(2)

def get_name_token(x):
    x = x.split('=')[-1]
    return x

def work(browser):
    num = 0
    x = 4
    y = -1
    patern_x_0 = '/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[9]/div[2]/table/tfoot/tr/td[2]/button'
    patern_x_1_0 = '/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[9]/div[2]/table/tbody/tr[{}]/td[1]/button'
    patern_x_2_0 = '/html/body/div[{}]/ul/li[{}]/label'
    patern_x_3_0 = '/html/body/div[{}]/div/ul/li[3]'

    token = get_name_token(browser.current_url)
    pattern = 'https://arpino.ru/admin/index.php?route=catalog/product/edit&user_token={}&product_id=117&filter_name=VINTAGE+БЕЗ+ОСТЕКЛЕНИЯ+BARSELONA'
    url = pattern.format(token)
    browser.get(url)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/form/ul/li[9]').click()

    while num != 10:
        num += 1
        x += 1
        y += 1
        patern_x_1 = patern_x_1_0.format(str(num))
        patern_x_2 = patern_x_2_0.format(str(x), str(keyss[y]))
        patern_x_3 = patern_x_3_0.format(str(x))

        browser.find_element(By.XPATH, patern_x_0).click()
        browser.find_element(By.XPATH, patern_x_1).click()
        browser.find_element(By.XPATH, patern_x_2).click()
        browser.find_element(By.XPATH, patern_x_3).click()

    patern_x_4_0 = '/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[9]/div[2]/table/tbody/tr[{}]/td[1]/a/img'
    patern_x_5_0 = '/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[9]/div[2]/table/tbody/tr[{}]/td[1]/div/div[2]/button[1]'

    num = 0
    y = -1

    while num != 10:
        num += 1
        y += 1
        patern_x_4 = patern_x_4_0.format(str(num))
        patern_x_5 = patern_x_5_0.format(str(num))
        browser.find_element(By.XPATH, patern_x_4).click()
        browser.find_element(By.XPATH, patern_x_5).click()
        browser.find_element(By.NAME, 'search').send_keys(name_photo[y] + Keys.ENTER)
        time.sleep(5)

def main():
    browser = webdriver.Firefox(options=options())
    browser.get('https://arpino.ru/admin')
    arpino_login(browser)
    work(browser)

if __name__ == '__main__':
    main()