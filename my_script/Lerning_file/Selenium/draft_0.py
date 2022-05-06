from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
browser.get('http://paintonline.editaraudio.com/')
ActionChains(browser).move_by_offset(250, 250).click().perform()