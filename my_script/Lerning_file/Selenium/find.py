from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Firefox()

def write_csv(data):
    with open('y.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['name', 'age', 'like', 'link']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_data():

    all_card = browser.find_elements(By.CLASS_NAME, 'iso_grid-5-item_full')

    for card in all_card:
        name = card.find_element(By.TAG_NAME, 'h4').text.strip()
        link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')

        try:
            age = card.find_element(By.CLASS_NAME, 'main_age_in_list').text.split()[0]
        except:
            age = 'нет данных'
        try:
            like = card.find_element(By.CLASS_NAME, 'main_vote_count').text.strip()
        except:
            like = 'нет данных'

        data = {'name': name, 'link': link, 'age': age, 'like': like}
        write_csv(data)

def main():
    pattern = 'https://ruskino.ru/art/groups/actresses?page={}'
    for i in range(1, 6):
        url = pattern.format(str(i))
        browser.get(url)
        get_data()
    browser.quit()

if __name__ == '__main__':
    main()