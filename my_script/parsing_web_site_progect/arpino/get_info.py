from selenium import webdriver
from selenium.webdriver.common.by import By
import os

ll = []
y = []

for top, dirs, files in os.walk('photo'):
    for nm in files:
        ll.append(os.path.join(nm))

for i in ll[:-2]:
    x = i[:-4]
    y.append(x)

name_photo = y[1:]



def options():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnotifications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = True
    return options

browser = webdriver.Firefox(options=options())
browser.get('https://radadoors.ru/mezhkomnatnye-dveri/mezhkomnatnaya-dver-barselona-sapele-8867/')

shpon_l = []
emal_spon_l = []
mdf_l = []

my_dict = {
    'Дуб альпийский': '26',
    'Дуб коньяк': '31',
    'Дуб горный': '30',
    'Дуб натуральный': '32',
    'Дуб шатто': '34',
    'Дуб старинный': '33',
    'Капучино': '35',
    'Латте': '37',
    'Табако': '44',
    'col. blanc МДФ': '49',
    'col. blanc ЯС': '66',
    'Сапеле': '41'
}

# получаю названия цветов шпона
pattern = '/html/body/content/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[{}]'
for i in range(1, 11):
    xp = pattern.format(str(i))
    try:
        browser.find_element(By.XPATH, xp).click()
        photo = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[5]/div[2]/div[1]/span').text
        shpon_l.append(photo)
    except:
        pass

# получаю названия цветов эмали шпона
pattern = '/html/body/content/div[1]/div[5]/div[2]/div[2]/div[2]/div[2]/div[{}]'
for i in range(1, 11):
    xp = pattern.format(str(i))
    try:
        browser.find_element(By.XPATH, xp).click()
        photo = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[5]/div[2]/div[1]/span').text
        emal_spon_l.append(photo)
    except:
        pass

# получаю названия цветов мдф
pattern = '/html/body/content/div[1]/div[5]/div[2]/div[2]/div[3]/div[2]/div[{}]'
for i in range(1, 11):
    xp = pattern.format(str(i))
    try:
        browser.find_element(By.XPATH, xp).click()
        photo = browser.find_element(By.XPATH, '/html/body/content/div[1]/div[5]/div[2]/div[1]/span').text
        mdf_l.append(photo)
    except:
        pass


mega_list = shpon_l + emal_spon_l + mdf_l
color = mega_list[1:]
num = len(shpon_l) + len(emal_spon_l) + len(mdf_l)
print(color)

keyss = []

for i in color:
    keyss.append(my_dict.setdefault(i))
print(keyss)

browser.close()
browser.quit()