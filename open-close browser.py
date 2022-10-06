import time
from selenium import webdriver

browser = webdriver.Chrome()
# driver = webdriver.Firefox()
browser.get('https://www.saucedemo.com/')
browser.maximize_window()  # Запуск браузера во весь экран
time.sleep(10)
browser.close()
