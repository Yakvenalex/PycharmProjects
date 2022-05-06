from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
pattern = 'https://ruskino.ru/art/groups/actresses?page={}'
actrises = []
for i in range(1, 151):
    url = pattern.format(str(i))
    browser.get(url)

    all_card = browser.find_elements(By.CLASS_NAME, 'iso_grid-5-item_full')
    for card in all_card:
       name = card.find_element(By.TAG_NAME, 'h4').text.strip()
       li = name.split()
       li = [li[1] + ' ' + li[0] + ' ' + 'инстаграм']
       li = str(li)[2:-2]
       actrises.append(li)

list_actris = actrises
browser.close()
browser.quit()