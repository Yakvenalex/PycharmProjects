from PIL import Image
import requests
from get_all_url_for_product_color import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def get_good_name(a):
    y = a.split('-')
    l = '_'.join(y[3:])
    return l[:-1]

def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = True
    return options

def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def get_pic_shpon(browser, num):
    names = get_good_name(browser.current_url)

    os.chdir('photo')

    url = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[3]/a').get_attribute('href')

    img = requests.get(url).content
    with open(f'{num}_{names}.jpg', 'wb') as file:
        file.write(img)
    print(f'фотография: {names}.jpg сохранена успешно!')

    os.chdir('..')

def get_pic_emal_shpon(browser, num):
    names = get_good_name(browser.current_url)

    os.chdir('photo')

    url = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[3]/a').get_attribute('href')

    img = requests.get(url).content
    with open(f'{num}_{names}.jpg', 'wb') as file:
        file.write(img)
    print(f'фотография: {names}.jpg сохранена успешно!')

    os.chdir('..')

def get_pic_mdf(browser, num):
    names = get_good_name(browser.current_url)

    os.chdir('photo')

    url = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[3]/a').get_attribute('href')

    img = requests.get(url).content
    with open(f'{num}_{names}.jpg', 'wb') as file:
        file.write(img)
    print(f'фотография: {names}.jpg сохранена успешно!')

    os.chdir('..')

def split():
    os.chdir('photo')

    li = os.listdir()[:-1]

    for i in li:
        im = Image.open(i)
        im_new = crop_center(im, 878, 1800)
        im_new.save(f'{i}', quality=90)

    for i in li:
        im = Image.open(i)
        im_new = im.resize((430, 855))
        im_new.save(f'{i}', quality=90)

    os.chdir('..')

def main():
        num = 999
        browser = webdriver.Firefox(options=options())
        for url in shpon_l:
            num += 1
            browser.get(url)
            get_pic_shpon(browser, num)

        for url in emal_spon_l:
            num += 1
            browser.get(url)
            get_pic_emal_shpon(browser, num)

        for url in mdf_l:
            num += 1
            browser.get(url)
            get_pic_mdf(browser, num)
        split()

        print('Работа скрипта завершена. Досвидания!')

        browser.close()
        browser.quit()

if __name__ == '__main__':
    main()