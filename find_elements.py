import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# driver = webdriver.Firefox()
browser.get('https://www.saucedemo.com/')
browser.maximize_window()  # Запуск браузера во весь экран
# user_name = browser.find_element_by_id('user-name') - устаревший поиск, стараться не использовать
# user_name = browser.find_element(By.ID, 'user-name') - поиск по ID
# user_name = browser.find_element(By.CSS_SELECTOR, '#user-name') - поиск по ID с помощью CSS-селектора
user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')  # Поиск по XPATH
user_name.send_keys('standard_user')
password = browser.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')
button_login = browser.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
browser.close()
