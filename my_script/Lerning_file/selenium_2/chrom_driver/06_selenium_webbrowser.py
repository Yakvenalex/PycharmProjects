from selenium import webdriver
from selenium_stealth import stealth
import time

def options():
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        return options

def stels(browser):
        stealth(browser,
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
                languages=["ru-RU", "ru"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)

def main():
        browser = webdriver.Chrome(options=options())
        stels(browser)
        browser.get('https://bot.sannysoft.com/')
        time.sleep(600)

if __name__ == '__main__':
    main()