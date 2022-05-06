import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/c/coolpropaganda/videos')

html = browser.find_element(By.TAG_NAME, 'html')
for i in range(1200):
    html.send_keys(Keys.DOWN)

all_videos = browser.find_elements(By.TAG_NAME, 'ytd-grid-video-renderer')
print(len(all_videos))